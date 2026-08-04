from rest_framework import serializers

from apps.bus.models import Bus


class BusCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ['plate', 'capacity']

    def validate_plate(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Plate cannnot be blank."
            )
        
        return value
    
    def validate_capacity(self, value):
        if value < 20:
            raise serializers.ValidationError(
                "Capacity must be at least 20."
            )
        
        return value