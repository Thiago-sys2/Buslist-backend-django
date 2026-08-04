from django.urls import path

from apps.user.views.auth_view import LoginView, RegisterView

urlpatterns = [
    path("resgister/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]