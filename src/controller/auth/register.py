from business.authentication import Authentication
from helpers import handle_errors, ParseResponse


class RegisterController:
    """
    RegisterController class with Register method
    """

    def __init__(self, register_data):
        self.username = register_data["username"]
        self.password = register_data["password"]
        self.city = register_data["city"]
        self.zipcode = register_data["zipcode"]
        self.obj_auth_business = Authentication(
            self.username, self.password, self.city, self.zipcode
        )
        self.response = ParseResponse()

    @handle_errors
    def register(self):
        "Method to register new user only (not admin)"
        response = self.obj_auth_business.username_exists()
        if not response:
            response = self.obj_auth_business.create_account()
            return self.response.success_response(response, 201)
