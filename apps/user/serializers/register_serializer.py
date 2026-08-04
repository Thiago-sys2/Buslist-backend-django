from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)

    email = serializers.EmailField()

    password = serializers.CharField(min_length=6, write_only=True)

    def validated_email(self, value):

        return value.strip().lower()

    def validaate_name(self, value):

        return value.strip()