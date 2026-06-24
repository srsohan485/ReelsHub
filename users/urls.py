from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView, FollowUnfollowView, SearchUserView  # ← SearchUserView যোগ করো

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowUnfollowView.as_view(), name='follow'),
    path('search/', SearchUserView.as_view(), name='search-user'),
]