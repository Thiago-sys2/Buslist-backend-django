from rest_framework import status
from rest_framework.exceptions import APIException

from core.error_messages import ErrorMessages


class BusNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ErrorMessages.BUS_NOT_FOUND

class BusAlreadyExistsException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = ErrorMessages.BUS_ALREADY_EXISTS

class BusInactiveException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ErrorMessages.BUS_INACTIVE

class BusAlreadyActiveException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ErrorMessages.BUS_ALREADY_ACTIVE

class BusAlreadyInactiveException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ErrorMessages.BUS_ALREADY_INACTIVE

class BusFullException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ErrorMessages.BUS_FULL

class BusUpdateInactiveException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = ErrorMessages.BUS_UPDATE_INACTIVE