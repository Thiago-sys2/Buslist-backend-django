from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.services.user_service import UserService
from core.exceptions.user_exceptions import InvalidCredentialsException


class AuthService:

    @staticmethod
    def register(validated_data):

        user = UserService.create(validated_data)

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user
        }

    @staticmethod
    def login(validated_data):

        email = validated_data["email"]

        password = validated_data["password"]

        user = authenticate(
            email=email,
            password=password
        )

        if user is None:
            raise InvalidCredentialsException()

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user
        }

        
