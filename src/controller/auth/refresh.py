from business.authentication import Authentication
from helpers import handle_errors, ParseResponse


class RefreshController:
    """
    Refresh Controller class containing refresh token generation method
    """

    def __init__(self, user_id, role):
        self.user_id = user_id
        self.role = role
        self.obj_auth_business = Authentication()
        self.response = ParseResponse()

    @handle_errors
    def refresh(self):
        response = self.obj_auth_business.refresh(self.user_id, self.role)
        return self.response.success_response(response)
