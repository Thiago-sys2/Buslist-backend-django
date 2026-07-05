from rest_framework import serializers
from apps.bus.models import Bus

class BusResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ['id', 'plate', 'capacity', 'active']