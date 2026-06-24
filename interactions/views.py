from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Like, Comment, SavedPost
from .serializers import CommentSerializer, SavedPostSerializer
from posts.models import Post

class LikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
            return Response({'message': 'Unliked'})
        return Response({'message': 'Liked'})

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        return Comment.objects.filter(post_id=post_id, parent=None)

class SavedPostToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        saved, created = SavedPost.objects.get_or_create(user=request.user, post=post)
        if not created:
            saved.delete()
            return Response({'message': 'Removed from saved'})
        return Response({'message': 'Post saved'})

class SavedPostListView(generics.ListAPIView):
    serializer_class = SavedPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedPost.objects.filter(user=self.request.user)