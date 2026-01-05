from django.urls import path
from .views import UserRegisterView, UserLoginView, UserMeView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("me/", UserMeView.as_view(), name="user-me"),
]

app_name = "user"
