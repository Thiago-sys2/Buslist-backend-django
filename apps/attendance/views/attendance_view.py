from rest_framework.views import APIView
from rest_framework.response import Response

from apps.attendance.serializers.attendance_response_serializer import AttendanceResponseSerializer
from apps.attendance.services.attendance_service import AttendanceService

class AttendanceDetailView(APIView):

    def get(self, request, trip_id, student_id):

        attendance = AttendanceService.find_by_student_and_trip(trip_id, student_id)

        serializer = AttendanceResponseSerializer(attendance)

        return Response(serializer.data)
    
class AttendanceListByTripView(APIView):

    def get(self, request, trip_id):

        attendance = AttendanceService.find_by_trip(trip_id)

        serializer = AttendanceResponseSerializer(attendance, many=True)

        return Response(serializer.data)
    
class AttendanceCountByTripView(APIView):

    def get(self, request, trip_id):

        count = AttendanceService.count_by_trip(trip_id)

        return Response(count)