from datetime import datetime
import logging
from config.config import Config
from db.database import db
from helpers import DataNotFound

logger = logging.getLogger(__name__)


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

        logger.info("Viewing history")

        data = db.get_items(Config.QUERY_TO_VIEW_HISTORY, (self.user_id,))
        if not data:
            raise DataNotFound(Config.NO_DATA)
        response = {}
        history_data = []
        for item in data:
            response = {
                "Date_time": item["date_time"],
                "Searched_for": item["searched_for"],
                "Searched_by": item["searched_by"],
                "City_name": item["city"],
            }
            history_data.append(response)
        return history_data

    def insert_history(self):
        """
        Function to insert history
        """

        logger.info("Inserting history")

        tm = datetime.now()
        date_time = tm.strftime(Config.FORMAT_DATE_TIME)
        searched_by = Config.CITY_NAME
        searched_for = Config.CURRENT_WEATHER
        query = Config.QUERY_TO_INSERT_SEARCH_HISTORY
        _id = db.add_item(
            query, (self.user_id, searched_for, searched_by, date_time, self.city)
        )
        return _id
