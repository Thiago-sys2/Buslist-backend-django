from rest_framework import serializers

from apps.trip.models import Trip
from apps.bus.models import Bus

class TripCreateSerializer(serializers.ModelSerializer):

    bus_id = serializers.PrimaryKeyRelatedField(
        source="bus",
        queryset=Bus.objects.all()
    )

    class Meta:
        model = Trip
        fields = ["date", "period", "bus_id"]