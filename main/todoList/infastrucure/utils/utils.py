from rest_framework.views import exception_handler
import logging
from rest_framework.response import Response

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    logger.warning("custom_exception_handler")

    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data["message"] = "Ops, Something bad happened"
        response.data["status_code"] = response.status_code
        code = response.status_code
        return Response(response.data, code)
