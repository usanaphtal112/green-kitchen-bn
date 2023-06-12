from django.urls import path

from .views import (
    SignUpView,
    LoginView,
    UserListView,
    UserDetailsView,
    LogoutAPIView,
    UserProfileView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("", UserListView.as_view(), name="user-list"),
    path("<int:user_id>/", UserDetailsView.as_view(), name="user-detail"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]
