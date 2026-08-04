from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers.login_serializer import LoginSerializer
from apps.user.serializers.register_serializer import RegisterSerializer
from apps.user.serializers.token_response_serializer import TokenResponseSerializer
from apps.user.services.auth_service import AuthService


class RegisterView(APIView):

    @extend_schema(
            tags=["Authentication"],
            summary="Register user",
            description="Registers a new user and returns JWT tokens.",
            request=RegisterSerializer,
            responses={
                201: TokenResponseSerializer,
                400: OpenApiResponse(description="Invalid data."),
                409: OpenApiResponse(description="Email already exists.")
            },
    )
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        result = AuthService.register(serializer.validated_data)

        response_serializer = TokenResponseSerializer(instance=result)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

class LoginView(APIView):

    @extend_schema(
            tags=["Authentication"],
            summary="Login",
            description="Authenticates a user and returns JWT tokens.",
            request=LoginSerializer,
            responses={
                200: TokenResponseSerializer,
                401: OpenApiResponse(description="Invalid credentials."),
        },
    )
    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        result = AuthService.login(serializer.validated_data)

        response_serializer = TokenResponseSerializer(instance=result)

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK
        )