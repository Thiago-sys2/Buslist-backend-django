from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.trip.serializers.trip_create_serializer import TripCreateSerializer
from apps.trip.serializers.trip_response_serializer import TripResponseSerializer
from apps.trip.services.trip_service import TripService


class TripCreateView(APIView):

    @extend_schema(
            tags=["Trip"],
            summary="Create trip",
            description="Creates a new trip in the system.",
            request=TripCreateSerializer,
            responses={
                201: TripResponseSerializer,
                400: OpenApiResponse(description="Invalid request data."),
                404: OpenApiResponse(description="Bus not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
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

    @extend_schema(
            tags=["Trip"],
            summary="Add student to trip",
            description="Adds a student to a trip.",
            responses={
                200: TripResponseSerializer,
                400: OpenApiResponse(description="Bus is already full."),
                404: OpenApiResponse(description="Trip or student not found."),
                409: OpenApiResponse(description="Student is already in this trip."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def post(self, request, trip_id, student_id):
        
        trip = TripService.add_student(trip_id, student_id)

        serializer = TripResponseSerializer(trip)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
class TripDetailView(APIView):
    
    @extend_schema(
            tags=["Trip"],
            summary="Find trip by ID",
            description="Returns a trip by its ID.",
            responses={
                200: TripResponseSerializer,
                404: OpenApiResponse(description="Trip not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request, id):

        trip = TripService.find_by_id(id)

        serializer = TripResponseSerializer(trip)

        return Response(serializer.data)

class TripListView(APIView):

    @extend_schema(
            tags=["Trip"],
            summary="List all trips",
            description="Returns a list of all registered trips.",
            responses={
                200: TripResponseSerializer(many=True),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request):

        trips = TripService.fin_all()

        serializer = TripResponseSerializer(trips, many=True)

        return Response(serializer.data)

class TripRemoveStudentView(APIView):

    @extend_schema(
            tags=["Trip"],
            summary="Remove student from trip",
            description="Removes a student from a trip.",
            responses={
                204: OpenApiResponse(description="Student removed successfully."),
                404: OpenApiResponse(description="Attendance not found for this student in this trip."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def delete(self, request, trip_id, student_id):
        
        TripService.remove_student_from_trip(trip_id, student_id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

