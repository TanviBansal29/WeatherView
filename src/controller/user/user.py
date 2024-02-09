from business.user import User
from helpers import ParseResponse, handle_errors


class UserController:
    "User Controller with user methods"

    def __init__(self, username=None, city=None):
        self.username = username
        self.city = city
        self.obj_user_business = User(username=self.username, city=self.city)
        self.response = ParseResponse()

    @handle_errors
    def view_user_data(self):
        """Returns user data"""

        data = self.obj_user_business.fetch_user_data()
        return self.response.success_response(data)

    @handle_errors
    def view_users(self):
        """
        Return list of uses with specified place name
        """

        data = self.obj_user_business.fetch_user_by_city()
        return self.response.success_response(data)
