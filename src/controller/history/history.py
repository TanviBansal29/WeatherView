from business.history import History
from helpers.custom_exceptions import DataNotFound
from helpers.rbac import access_control


class HistoryController:
    "History Controller containing methods to view user search histroy"

    def __init__(self, user_id, city=None):
        self.user_id = user_id
        self.city = city
        self.obj_history_business = History(self.user_id, city=self.city)

    def view_user_history(self):
        """
        Returns user search history
        """
        try:
            data = self.obj_history_business.view_history()
            return data
        except DataNotFound as e:
            return {"status": 404, "message": str(e)}, 404
