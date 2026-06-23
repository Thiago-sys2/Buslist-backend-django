from rest_framework import serializers
from apps.bus.models import Bus

class BusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = [
            'capacity',
            'active'
        ]

    def validate_capacity(self, value):
        if value < 20:
            raise serializers.ValidationError(
                "Capacity must be at least 20."
            )
        
        return value