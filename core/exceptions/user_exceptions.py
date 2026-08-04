from rest_framework.exceptions import APIException
from rest_framework import status

from core.error_messages import ErrorMessages

class UserNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ErrorMessages.USER_NOT_FOUND

class EmailAlreadyExistsException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = ErrorMessages.EMAIL_ALREADY_EXISTS

class InvalidCredentialsException(APIException):
    status_code = status.HTTP_409_CONFLICT,
    default_detail = ErrorMessages.INVALID_CREDENTIALS