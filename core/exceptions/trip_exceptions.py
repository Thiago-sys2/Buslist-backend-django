from rest_framework.exceptions import APIException
from rest_framework import status

from core.error_messages import ErrorMessages

class TripNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ErrorMessages.TRIP_NOT_FOUND