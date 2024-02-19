from helpers import handle_errors, ParseResponse
from business.authentication import Authentication


class LoginController:
    """
    LoginController class with Login method
    """

    def __init__(self, login_data):
        self.username = login_data["username"]
        self.password = login_data["password"]
        self.obj_auth_business = Authentication(self.username, self.password)
        self.response = ParseResponse()

    @handle_errors
    def login(self):
        """Method for user login"""
        if self.obj_auth_business.verify_user():
            data = self.obj_auth_business.get_role()
            role = data.get("role")
            user_id = data.get("user_id")
            token = self.obj_auth_business.generate_token(role, user_id)
            return self.response.success_response(token)
