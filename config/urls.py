from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path("bus/", include("apps.bus.urls")),
    path("student/", include("apps.student.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("trip/", include("apps.trip.urls")),
]
