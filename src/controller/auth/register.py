from business.authentication import Authentication
from helpers.custom_exceptions import DataAlreadyExists, DataNotFound


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

    def register(self):
        "Method to register new user only (not admin)"

        try:
            result = self.obj_auth_business.verify_username()

            if not result:
                self.obj_auth_business.create_account()
                response = {"status_code": 201, "message": "SIGNED UP SUCCESSFULLY"}
                return response

        except DataAlreadyExists as e:
            return {"status": 409, "message": str(e)}, 409
