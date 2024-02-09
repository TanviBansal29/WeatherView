from business.history import History
from helpers import handle_errors, ParseResponse


class HistoryController:
    "History Controller containing methods to view user search histroy"

    def __init__(self, user_id, city=None):
        self.user_id = user_id
        self.city = city
        self.obj_history_business = History(self.user_id, city=self.city)
        self.response = ParseResponse()

    @handle_errors
    def view_user_history(self):
        """
        Returns user search history
        """

        response = self.obj_history_business.view_history()
        return self.response.success_response(response)
