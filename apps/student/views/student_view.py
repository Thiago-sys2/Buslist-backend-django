from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.student.serializers.student_create_serializer import StudentCreateSerializer
from apps.student.serializers.student_response_serializer import StudentResponseSerializer
from apps.student.serializers.student_update_serializer import StudentUpdateSerializer
from apps.student.services.student_service import StudentService

class StudentCreateView(APIView):

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

    def get(self, request, id):

        student = StudentService.find_by_id(id)

        serializer = StudentResponseSerializer(student)

        return Response(serializer.data)
    
class StudentListView(APIView):

    def get(self, request):

        students = StudentService.find_all()

        serializer = StudentResponseSerializer(students, many=True)

        return Response(serializer.data)
    
class StudentUpdateView(APIView):

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

    def delete(self, request, id):

        StudentService.delete(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
