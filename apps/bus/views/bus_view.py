from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.bus.serializers.bus_create_serializer import BusCreateSerializer
from apps.bus.serializers.bus_response_serializer import BusResponseSerializer
from apps.bus.serializers.bus_update_serializer import BusUpdateSerializer
from apps.bus.services.bus_service import BusService


class BusCreateView(APIView):

    @extend_schema(
            tags=["Bus"],
            summary="Create Bus",
            description="Create a new bus",
            request=BusCreateSerializer,
            responses={
                201: BusResponseSerializer,
                400: OpenApiResponse(description="Invalid request data."),
                409: OpenApiResponse(description="A bus with this license plate already exists."),
                500: OpenApiResponse(description="Internal server error."),
            }

    )
    def post(self, request):
        
        serializer = BusCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        bus = BusService.create(serializer.validated_data)

        response = BusResponseSerializer(bus)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED
        )
    
class BusDetailView(APIView):

    @extend_schema(
            tags=["Bus"],
            summary="Find bus by ID",
            description="Returns a bus by its ID.",
            responses={
                200: BusResponseSerializer,
                404: OpenApiResponse(description="Bus not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request, id):

        bus = BusService.find_by_id(id)

        serializer = BusResponseSerializer(bus)

        return Response(serializer.data)
    
class BusListView(APIView):

    @extend_schema(
            tags=["Bus"],
            summary="List all buses",
            description="Returns a list of all registered buses.",
            responses={
                200: BusResponseSerializer(many=True),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def get(self, request):

        buses = BusService.find_all()

        serializer = BusResponseSerializer(buses, many=True)

        return Response(serializer.data)
    
class BusUpdateView(APIView):
    
    @extend_schema(
            tags=["Bus"],
            summary="Update bus",
            description="Updates an existing bus.",
            request=BusUpdateSerializer,
            responses={
                200: BusResponseSerializer,
                400: OpenApiResponse(description="Invalid request data."),
                404: OpenApiResponse(description="Bus not found."),
                409: OpenApiResponse(description="There's already a bus with that license plate."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def put(self, request, id):

        serializer = BusUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        bus = BusService.update(
            id,
            serializer.validated_data
        )

        response = BusResponseSerializer(bus)

        return Response(response.data)
    
class BusDeactivateView(APIView):
    
    @extend_schema(
            tags=["Bus"],
            summary="Deactivate bus",
            description="Deactivates an active bus.",
            responses={
                204: OpenApiResponse(description="Bus deactivated successfully."),
                404: OpenApiResponse(description="Bus not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def patch(self, request, id):

        BusService.desactive(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    
class BusReactivateView(APIView):

    @extend_schema(
            tags=["Bus"],
            summary="Activate bus",
            description="Activates an inactive bus.",
            responses={
                204: OpenApiResponse(description="Bus activated successfully."),
                404: OpenApiResponse(description="Bus not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def patch(self, request, id):

        BusService.reactivate(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class BusDeleteView(APIView):

    @extend_schema(
            tags=["Bus"],
            summary="Delete bus",
            description="Deletes a bus from the system.",
            responses={
                204: OpenApiResponse(description="Bus deleted successfully."),
                404: OpenApiResponse(description="Bus not found."),
                500: OpenApiResponse(description="Internal server error.")
            }
    )
    def delete(self, request, id):

        BusService.delete(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )