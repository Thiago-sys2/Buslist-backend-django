from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.attendance.serializers.attendance_response_serializer import (
    AttendanceResponseSerializer,
)
from apps.attendance.services.attendance_service import AttendanceService


class AttendanceDetailView(APIView):

    @extend_schema(
            tags=["Attendance"],
            summary="Find attendance by trip and student",
            description="Returns the attendance record of a specific student in a specific trip.",
            responses={
                200: AttendanceResponseSerializer,
                404: OpenApiResponse(description="Attendance not found for this student in this trip."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request, trip_id, student_id):

        attendance = AttendanceService.find_by_student_and_trip(trip_id, student_id)

        serializer = AttendanceResponseSerializer(attendance)

        return Response(serializer.data)
    
class AttendanceListByTripView(APIView):

    @extend_schema(
            tags=["Attendance"],
            summary="List attendances by trip",
            description="Returns all attendance records for a specific trip.",
            responses={
                200: AttendanceResponseSerializer(many=True),
                404: OpenApiResponse(description="Trip not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request, trip_id):

        attendance = AttendanceService.find_by_trip(trip_id)

        serializer = AttendanceResponseSerializer(attendance, many=True)

        return Response(serializer.data)
    
class AttendanceCountByTripView(APIView):

    @extend_schema(
            tags=["Attendance"],
            summary="Count students in a trip",
            description="Returns the total number of students assigned to a specific trip.",
            responses={
                200: OpenApiResponse(description="Number of students returned successfully."),
                404: OpenApiResponse(description="Trip not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request, trip_id):

        count = AttendanceService.count_by_trip(trip_id)

        return Response(count)