from apps.attendance.models import Attendance
from apps.attendance.services.attendance_service import AttendanceService
from apps.student.services.student_service import StudentService
from apps.trip.models import Trip
from core.exceptions.bus_exceptions import BusFullException, BusInactiveException
from core.exceptions.student_exceptions import StudentAlreadyInTripException
from core.exceptions.trip_exceptions import TripNotFoundException


class TripService:

    @staticmethod
    def create(validate_data):
        
        bus = validate_data["bus"]

        if not bus.active:
            raise BusInactiveException()
        
        trip = Trip.objects.create(
            date=validate_data["date"],
            period=validate_data["period"],
            bus=bus
        )

        return trip
    
    @staticmethod
    def find_by_id(trip_id):

        try:
            return Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            raise TripNotFoundException()
    
    @staticmethod
    def fin_all():
        return Trip.objects.all()
    
    @staticmethod
    def add_student(trip_id, student_id):
        
        trip = TripService.find_by_id(trip_id)
        student = StudentService.find_by_id(student_id)

        if Attendance.objects.filter(trip_id=trip_id, student_id=student_id).exists():
            raise StudentAlreadyInTripException()
        
        current_occupation = AttendanceService.count_by_trip(trip_id)

        if current_occupation >= trip.bus.capacity:
            raise BusFullException()
        
        Attendance.objects.create(
            trip=trip,
            student=student,
            gift=True
        )

        return trip
    
    @staticmethod
    def remove_student_from_trip(trip_id, student_id):

        attendance = AttendanceService.find_by_student_and_trip(student_id, trip_id)

        attendance.delete()

        




        

