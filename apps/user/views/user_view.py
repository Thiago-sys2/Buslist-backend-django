from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from typing import Any, cast

from apps.user.serializers.user_create_serializer import UserCreateSerializer
from apps.user.serializers.user_response_serializer import UserResponseSerializer
from apps.user.serializers.user_update_serializer import UserUpdateSerializer
from apps.user.services.user_service import UserService

class UserCreateView(APIView):

    @extend_schema(
            tags=["User"],
            summary="Create user",
            description="Creates a new user in the system.",
            request=UserCreateSerializer,
            responses={
                201: UserResponseSerializer,
                400: OpenApiResponse(description="Invalid data."),
                409: OpenApiResponse(description="Email already exists."),
            },
    )
    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = UserService.create(serializer.validated_data)

        response = UserResponseSerializer(user)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED
        )
    
class UserListView(APIView):

    @extend_schema(
            tags=["User"],
            summary="List users",
            description="Returns all users.",
            responses={
                200: UserResponseSerializer(many=True)
            },
    )
    def get(self, request):

        users = UserService.find_all()

        serializer = UserResponseSerializer(users, many=True)

        return Response(serializer.data)
    
class UserDetailView(APIView):

    @extend_schema(
            tags=["User"],
            summary="Find user by id",
            description="Returns a user by its id.",
            responses={
                200: UserResponseSerializer,
                404: OpenApiResponse(description="User not found."),
            },
    )
    def get(self, request, id):
        
        user = UserService.find_by_id(id)

        serializer = UserResponseSerializer(user)

        return Response(serializer.data)
    
class UserUpdateView(APIView):

    @extend_schema(
            tags=["User"],
            summary="Update user",
            description="Updates a user.",
            request=UserUpdateSerializer,
            responses={
                200: UserResponseSerializer,
                404: OpenApiResponse(description="User not found."),
                409: OpenApiResponse(description="Email already exists."),
        },
    )
    def put(self, request, id):

        serializer = UserUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        validated_data = cast(dict[str, Any], serializer.validated_data)

        user = UserService.update(
            id,
            validated_data
        )

        response = UserResponseSerializer(user)

        return Response(response.data)
    
class UserDeleteView(APIView):

    @extend_schema(
            tags=["User"],
            summary="Delete user",
            description="Deactivates a user.",
            responses={
                204: OpenApiResponse(description="User deleted successfully."),
                404: OpenApiResponse(description="User not found."),
        },
    )
    def delete(self, request, id):

        UserService.delete(id)

        return Response(
            status = status.HTTP_204_NO_CONTENT
        )