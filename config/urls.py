from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("bus/", include("apps.bus.urls")),
    path("student/", include("apps.student.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("trip/", include("apps.trip.urls")),
    path("user/", include("apps.user.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
