from datetime import datetime
from config.config import Config
from db.database import db
from helpers import DataNotFound


class History:
    """
    Class to provide view and insert history
    """

    def __init__(self, user_id, city=None):
        self.user_id = user_id
        self.city = city

    def view_history(self):
        """
        Function to view user history
        """
        data = db.get_items(Config.QUERY_TO_VIEW_HISTORY, (self.user_id,))
        if not data:
            raise DataNotFound("No data found")
        return data

    def insert_history(self):
        """
        Function to insert history
        """
        tm = datetime.now()
        date_time = tm.strftime(Config.FORMAT_DATE_TIME)
        searched_by = Config.CITY_NAME
        searched_for = Config.CURRENT_WEATHER
        query = Config.QUERY_TO_INSERT_SEARCH_HISTORY
        _id = db.add_item(
            query, (self.user_id, searched_for, searched_by, date_time, self.city)
        )
        return _id
