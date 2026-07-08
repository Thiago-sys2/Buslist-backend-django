from rest_framework.exceptions import APIException
from rest_framework import status

from core.error_messages import ErrorMessages

class StudentNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ErrorMessages.STUDENT_NOT_FOUND

class StudentAlreadyInTripException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = ErrorMessages.STUDENT_ALREADY_IN_TRIP

class StudentAlreadyExistsCPFException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = ErrorMessages.STUDENT_ALREADY_EXISTS_CPF