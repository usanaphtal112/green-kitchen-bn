from django.urls import path

from .views import SignUpView, LoginView, UserListView, UserDetailsView


urlpatterns = [
    path("users/signup/", SignUpView.as_view(), name="signup"),
    path("users/login/", LoginView.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:user_id>/", UserDetailsView.as_view(), name="user-detail"),
]
