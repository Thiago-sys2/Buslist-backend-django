from django.urls import path

from apps.attendance.views.attendance_view import (
    AttendanceDetailView,
    AttendanceListByTripView,
    AttendanceCountByTripView,
)

urlpatterns = [
    
    path(
        "trip/<int:trip_id>/student/<int:student_id>/",
        AttendanceDetailView.as_view(),
        name="attendance-details",
    ),

    path(
        "trip/<int:trip_id>/",
        AttendanceListByTripView.as_view(),
        name="attendance-list",
    ),

    path(
        "trip;<int:trip_id>/count/",
        AttendanceCountByTripView.as_view(),
        name="attendance-count",
    ),
]