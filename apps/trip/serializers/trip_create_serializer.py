from rest_framework import serializers

from apps.bus.models import Bus
from apps.trip.models import Trip


class TripCreateSerializer(serializers.ModelSerializer):

    bus_id = serializers.PrimaryKeyRelatedField(
        source="bus",
        queryset=Bus.objects.all()
    )

    class Meta:
        model = Trip
        fields = ["date", "period", "bus_id"]