from django.urls import path
from .views import LikeToggleView, CommentCreateView, CommentListView, SavedPostToggleView, SavedPostListView

urlpatterns = [
    path('like/<int:pk>/', LikeToggleView.as_view(), name='like-toggle'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentListView.as_view(), name='comment-list'),
    path('save/<int:pk>/', SavedPostToggleView.as_view(), name='save-toggle'),
    path('saved/', SavedPostListView.as_view(), name='saved-list'),
]