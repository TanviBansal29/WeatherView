from flask_jwt_extended import get_jwt, verify_jwt_in_request
from helpers import ParseResponse, Unauthorized


response = ParseResponse()


def access_control(*role):
    def inner(func):
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            jwt = get_jwt()
            get_role = jwt["role"]
            if get_role in role:
                return func(*args, **kwargs)
            else:
                return response.error_response(
                    Unauthorized,
                    message="You are not authorized to access these resource.",
                )

        return wrapper

    return inner
