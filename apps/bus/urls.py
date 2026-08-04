from django.urls import path

from apps.bus.views.bus_view import (
    BusCreateView,
    BusDeactivateView,
    BusDeleteView,
    BusDetailView,
    BusListView,
    BusReactivateView,
    BusUpdateView,
)

urlpatterns = [
    
    path(
        "",
        BusCreateView.as_view(),
        name="bus-create",
    ),

    path(
        "<int:id>/",
        BusDetailView.as_view(),
        name="bus-details",
    ),
    path(
        "all/",
        BusListView.as_view(),
        name="bus-list",
    ),

    path(
        "<int:id>/update/",
        BusUpdateView.as_view(),
        name="bus-update",
    ),

    path(
        "<int:id>/deactivate/",
        BusDeactivateView.as_view(),
        name="bus-deactivate",
    ),

    path(
        "<int:id>/reactivate/",
        BusReactivateView.as_view(),
        name="bus-reactivate",
    ),

    path(
        "<int:id>/delete/",
        BusDeleteView.as_view(),
        name="bus-delete",
    ),
]