from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, serializers
from .models import FCMToken, Notification

class FCMTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMToken
        fields = ['token']

class RegisterFCMTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = request.data.get('token')
        FCMToken.objects.update_or_create(user=request.user, defaults={'token': token})
        return Response({'message': 'Token saved'})

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read', 'created_at']

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class MarkReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        Notification.objects.filter(pk=pk, recipient=request.user).update(is_read=True)
        return Response({'message': 'Marked as read'})