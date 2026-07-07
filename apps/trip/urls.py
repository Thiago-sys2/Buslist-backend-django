from django.urls import path

from apps.trip.views.trip_view import (
    TripCreateView,
    TripAddStudentView,
    TripDetailView,
    TripListView,
    TripRemoveStudentView,
)

urlpatterns = [

    path(
        "",
        TripCreateView.as_view(),
        name="trip-create",
    ),

    path(
        "<int:trip_id>/students/<int:student_id>/",
        TripAddStudentView.as_view(),
        name="trip-add-student",
    ),

    path(
        "<int:id>/",
        TripDetailView.as_view(),
        name="trip-details",
    ),

    path(
        "all/",
        TripListView.as_view(),
        name="trip_list"
    ),

    path(
        "<int:trip_id>/students/<int:student_id>/remove/",
        TripRemoveStudentView.as_view(),
        name="trip-remove-student",
    ),
]