from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.trip.serializers.trip_create_serializer import TripCreateSerializer
from apps.trip.serializers.trip_response_serializer import TripResponseSerializer
from apps.trip.services.trip_service import TripService

class TripCreateView(APIView):

    def post(self, request):

        serializer = TripCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        trip = TripService.create(serializer.validated_data)

        response = TripResponseSerializer(trip)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED
        )

class TripAddStudentView(APIView):

    def post(self, request, trip_id, student_id):
        
        trip = TripService.add_student(trip_id, student_id)

        serializer = TripResponseSerializer(trip)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
class TripDetailView(APIView):
    
    def get(self, request, id):

        trip = TripService.find_by_id(id)

        serializer = TripResponseSerializer(trip)

        return Response(serializer.data)
    
class TripRemoveStudentView(APIView):

    def delete(self, request, trip_id, student_id):
        
        TripService.remove_student_from_trip(trip_id, student_id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

