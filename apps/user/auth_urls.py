from django.urls import path

from apps.user.views.auth_view import LoginView, RefreshView, RegisterView

urlpatterns = [
    
    path(
        "resgister/",
         RegisterView.as_view(),
         name="register"
    ),
    path(
        "login/",
         LoginView.as_view(),
         name="login"
    ),
    path(
        "refresh/",
        RefreshView.as_view(),
        name="refresh"
    ),
]