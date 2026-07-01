from apps.attendance.models import Attendance
from rest_framework.exceptions import NotFound

class AttendanceService:

    @staticmethod
    def find_by_student_and_trip(student_id, trip_id):

        try:
            return Attendance.objects.get(student_id=student_id, trip_id=trip_id)
        except Attendance.DoesNotExist:
            raise NotFound(
                "Attendance not found for this student in this trip."
            )
        
    @staticmethod
    def find_by_trip(trip_id):

        return Attendance.objects.filter(trip_id=trip_id)
    
    @staticmethod
    def count_by_trip(trip_id):
        
        return Attendance.objects.filter(trip_id=trip_id).count()
