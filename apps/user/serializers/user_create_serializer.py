from rest_framework import serializers

from apps.user.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=18
    )

    class Meta:
        model = User
        fields = ["name", "email", "password"]