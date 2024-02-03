from typing import Dict
from flask_smorest import abort
from flask_jwt_extended import create_access_token, create_refresh_token
from helpers.custom_exceptions import InvalidCredentials
from business.authentication import Authentication


class LoginController:
    """
    LoginController class with Login method
    """

    def __init__(self, login_data):
        self.username = login_data["username"]
        self.password = login_data["password"]
        self.obj_auth_business = Authentication(self.username, self.password)

    def login(self):
        """Method for user login"""
        try:
            result = self.obj_auth_business.verify_user()

            if result:
                data = self.obj_auth_business.get_role()
                role = data["role"]
                user_id = data["user_id"]
                return self.obj_auth_business.generate_token(role, user_id)

        except InvalidCredentials as e:
            return {"status": 401, "message": str(e)}
