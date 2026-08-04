from django.urls import path

from apps.student.views.student_view import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
)

urlpatterns = [

    path(
        "",
        StudentCreateView.as_view(),
        name="student-create",
    ),

    path(
        "<int:id>/",
        StudentDetailView.as_view(),
        name="student-detail",
    ),

    path(
        "all/",
        StudentListView.as_view(),
        name="student-list",
    ),

    path(
        "<int:id>/update/",
        StudentUpdateView.as_view(),
        name="student-update",
    ),

    path(
        "<int:id>/delete/",
        StudentDeleteView.as_view(),
        name="student-delete",
    ),
]