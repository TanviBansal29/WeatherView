from business.authentication import Authentication
from helpers import handle_errors


class LogoutController:
    """
    Logout Controller class containing logout method
    """

    def __init__(self, token_id):
        self.token_id = token_id
        self.obj_auth_business = Authentication()

    @handle_errors
    def logout(self):
        response = self.obj_auth_business.logout(self.token_id)
        return self.response.success_response(response)
