from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers.login_serializer import LoginSerializer
from apps.user.serializers.refresh_serializer import RefreshSerializer
from apps.user.serializers.register_serializer import RegisterSerializer
from apps.user.serializers.token_response_serializer import TokenResponseSerializer
from apps.user.services.auth_service import AuthService


class RegisterView(APIView):

    permission_classes = [AllowAny]

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

    permission_classes = [AllowAny]

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

class RefreshView(APIView):

    permission_classes = [AllowAny]

    @extend_schema(
            tags=["Authentication"],
            summary="Refresh access token",
            description="Generates a new access token using a valid refresh token.",
            request=RefreshSerializer,
            responses={
                200: OpenApiResponse(description="Access token generated successfully."),
                401: OpenApiResponse(description="Invalid or expired refresh token."),
        },
    )
    def post(self, request):

        serializer = RefreshSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        result = AuthService.refresh(serializer.validated_data)

        return Response(
            result,
            status=status.HTTP_200_OK
        )