from django.urls import path
from .views import RegisterFCMTokenView, NotificationListView, MarkReadView

urlpatterns = [
    path('register-token/', RegisterFCMTokenView.as_view(), name='register-token'),
    path('', NotificationListView.as_view(), name='notification-list'),
    path('read/<int:pk>/', MarkReadView.as_view(), name='mark-read'),
]