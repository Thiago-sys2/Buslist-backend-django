from rest_framework import serializers

from apps.user.models import User


class UserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "name", "email", "role", "is_active", "created_at", "updated_at"]