from django.urls import path

from apps.user.views.user_view import (
    UserCreateView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
)

urlpatterns = [
    
    path(
        "",
        UserCreateView.as_view(),
        name="user-create"
    ),

    path(
        "all/",
        UserListView.as_view(),
        name="user-list"
    ),

    path(
        "<int:id>",
        UserDetailView.as_view(),
        name="user-detail"
    ),

    path(
        "<int:id>/update/",
        UserUpdateView.as_view(),
        name="user-update"
    ),

    path(
        "<int:id>/delete/",
        UserDeleteView.as_view(),
        name="user-delete"
    )
]