from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, SearchPostView  # ← SearchPostView যোগ করো

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchPostView.as_view(), name='search-post'),
]