from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.student.serializers.student_create_serializer import StudentCreateSerializer
from apps.student.serializers.student_response_serializer import (
    StudentResponseSerializer,
)
from apps.student.serializers.student_update_serializer import StudentUpdateSerializer
from apps.student.services.student_service import StudentService
from apps.user.permissions.role_permissions import IsAdmin


class StudentCreateView(APIView):

    permission_classes = [IsAdmin]

    @extend_schema(
            tags=["Student"],
            summary="Create student",
            description="Creates a new student in the system.",
            request=StudentCreateSerializer,
            responses={
                201: StudentResponseSerializer,
                400: OpenApiResponse(description="Invalid request data."),
                409: OpenApiResponse(description="CPF already registered."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def post(self, request):

        serializer = StudentCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        student = StudentService.create(serializer.validated_data)

        response = StudentResponseSerializer(student)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED
        )

class StudentDetailView(APIView):

    @extend_schema(
            tags=["Student"],
            summary="Find in student by ID",
            description="Returns a student by its ID.",
            responses={
                200: StudentResponseSerializer,
                404: OpenApiResponse(description="Student not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request, id):

        student = StudentService.find_by_id(id)

        serializer = StudentResponseSerializer(student)

        return Response(serializer.data)
    
class StudentListView(APIView):

    @extend_schema(
            tags=["Student"],
            summary="List all students",
            description="Returns a list of all registered students.",
            responses={
                200: StudentResponseSerializer(many=True),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request):

        students = StudentService.find_all()

        serializer = StudentResponseSerializer(students, many=True)

        return Response(serializer.data)
    
class StudentUpdateView(APIView):

    permission_classes = [IsAdmin]

    @extend_schema(
            tags=["Student"],
            summary="Update student",
            description="Updates an existing student.",
            request=StudentUpdateSerializer,
            responses={
                200: StudentResponseSerializer,
                400: OpenApiResponse(description="Invalid request data."),
                404: OpenApiResponse(description="Student not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def put(self, request, id):
        
        serializer = StudentUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        student = StudentService.update(
            id,
            serializer.validated_data
        )

        response = StudentResponseSerializer(student)

        return Response(response.data)
    
class StudentDeleteView(APIView):

    permission_classes = [IsAdmin]

    @extend_schema(
            tags=["Student"],
            summary="Delete student",
            description="Deletes a student from the system.",
            responses={
                204: OpenApiResponse(description="Student deleted successfully."),
                404: OpenApiResponse(description="Student not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def delete(self, request, id):

        StudentService.delete(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
