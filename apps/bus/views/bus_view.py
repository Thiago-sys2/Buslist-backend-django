from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.bus.serializers.bus_create_serializer import BusCreateSerializer
from apps.bus.serializers.bus_response_serializer import BusResponseSerializer
from apps.bus.serializers.bus_update_serializer import BusUpdateSerializer
from apps.bus.services.bus_service import BusService

class BusCreateView(APIView):

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

    def get(self, request, id):

        bus = BusService.find_by_id(id)

        serializer = BusResponseSerializer(bus)

        return Response(serializer.data)
    
class BusListView(APIView):

    def get(self, request):

        buses = BusService.find_all()

        serializer = BusResponseSerializer(buses, many=True)

        return Response(serializer.data)
    
class BusUpdate(APIView):
    
    def put(self, request, id):

        serializer = BusUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        bus = BusService.update(
            id,
            serializer.validated_data
        )

        response = BusResponseSerializer(bus)

        return Response(response.data)
    
class BusDesactiveView(APIView):
    
    def patch(self, request, id):

        BusService.desactive(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    
class BusDeleteView(APIView):

    def delete(self, request, id):

        BusService.delete(id)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )