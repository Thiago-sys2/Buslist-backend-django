from apps.bus.models import Bus
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound


class BusService:

    @staticmethod
    def create(validated_data):
        
        plate = validated_data["plate"]
        capacity = validated_data["capacity"]

        if Bus.objects.filter(plate=plate).exists():
            raise ValidationError("There's already a bus with that license plate!")
        
        bus = Bus.objects.create(
            plate=plate,
            capacity=capacity,
        )

        return bus
    
    @staticmethod
    def find_by_id(bus_id):
        
        try:
            return Bus.objects.get(id=bus_id)
        except Bus.DoesNotExist:
            raise NotFound("Bus not found.")
        
    @staticmethod
    def find_all():
        return Bus.objects.all()
    
    @staticmethod
    def update(bus_id, validate_data):

        bus = BusService.find_by_id(bus_id)

        if not bus.active:
            raise ValidationError(
                "Cannot update an inactive bus."
            )
        
        if "plate" in validate_data:
            plate = validate_data["plate"]

            if Bus.objects.filter(plate=plate).exclude(id=bus.id).exists(): 
                raise ValidationError(
                    "There's already a bus with that license plate."
                )
            
            bus.plate = plate
        
        if "capacity" in validate_data:
            bus.capacity = validate_data["capacity"]

        bus.save()

        return bus

    @staticmethod
    def desactive(bus_id):

        bus = BusService.find_by_id(bus_id)

        bus.active = False
        bus.save()

        return bus
    
    @staticmethod
    def reactivate(bus_id):

        bus = BusService.find_by_id(bus_id)

        bus.active = True
        bus.save()

        return bus
    
    @staticmethod
    def delete(bus_id):

        bus = BusService.find_by_id(bus_id)

        bus.delete()