from apps.attendance.models import Attendance
from core.exceptions.attendance_exceptions import AttendanceNotFoundException


class AttendanceService:

    @staticmethod
    def find_by_student_and_trip(trip_id, student_id):

        try:
            return Attendance.objects.get(trip_id=trip_id, student_id=student_id)
        except Attendance.DoesNotExist:
            raise AttendanceNotFoundException()
        
    @staticmethod
    def find_by_trip(trip_id):

        return Attendance.objects.filter(trip_id=trip_id)
    
    @staticmethod
    def count_by_trip(trip_id):
        
        return Attendance.objects.filter(trip_id=trip_id).count()
