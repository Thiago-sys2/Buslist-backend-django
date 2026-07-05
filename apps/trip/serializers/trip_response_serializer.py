from rest_framework import serializers

from apps.bus.serializers.bus_response_serializer import BusResponseSerializer
from apps.trip.models import Trip

class TripResponseSerializer(serializers.ModelSerializer):
    
    bus = BusResponseSerializer()
    total_students = serializers.IntegerField()
    
    class Meta:
        model = Trip
        fields = ["id", "date", "period", "bus", "total_students"]
        