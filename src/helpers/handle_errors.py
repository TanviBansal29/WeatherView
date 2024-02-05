from functools import wraps

from helpers.custom_exceptions import (
    DataAlreadyExists,
    InvalidCredentials,
    DuplicateEntryError,
    DataNotFound,
)
from helpers.parse_response import ParseResponse


def handle_errors(handler_function):
    """Handle errors decorator to catch all errors raised in business layer"""

    @wraps(handler_function)
    def wrapper(*args, **kwargs):
        response = ParseResponse()
        try:
            return handler_function(*args, **kwargs)

        except DataAlreadyExists as err:
            return response.error_response(DataAlreadyExists, str(err))

        except InvalidCredentials as err:
            return response.error_response(InvalidCredentials, str(err))

        except DuplicateEntryError as err:
            return response.error_response(DuplicateEntryError, str(err))

        except DataNotFound as err:
            return response.error_response(DataNotFound, str(err))

        except Exception as err:
            return {
                "message": str(err),
                "status_code": 500,
            }, 500

    return wrapper
