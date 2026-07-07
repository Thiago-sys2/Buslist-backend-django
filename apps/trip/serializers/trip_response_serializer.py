from rest_framework import serializers
from apps.attendance.models import Attendance
from apps.bus.serializers.bus_response_serializer import BusResponseSerializer
from apps.trip.models import Trip

class TripResponseSerializer(serializers.ModelSerializer):
    
    bus = BusResponseSerializer()
    total_students = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = ["id", "date", "period", "bus", "total_students"]
    
    def get_total_students(self, obj):
        return Attendance.objects.filter(trip=obj).count()
        