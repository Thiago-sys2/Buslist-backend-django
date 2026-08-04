from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Internal server error." 
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    data = response.data or {}

    return Response(
        {
            "status": response.status_code,
            "message": data.get("detail", data) if isinstance(data, dict) else data
        },
        status=response.status_code
    )