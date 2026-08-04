from rest_framework import serializers

from apps.user.serializers.user_response_serializer import UserResponseSerializer


class TokenResponseSerializer(serializers.Serializer):

    access = serializers.CharField()

    refresh = serializers.CharField()

    user = UserResponseSerializer()