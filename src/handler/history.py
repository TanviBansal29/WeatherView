import logging
from datetime import datetime
from config.config import Config
from db.database import db

logger = logging.getLogger(__name__)

class History:
    """
        Class to provide view and insert history
    """
    def __init__(self,user_id, city=None):
        self.user_id = user_id
        self.city = city

    def view_history(self):
        """
            Function to view user history
        """
        logger.debug(Config.HISTORY_VIEW, self.user_id)
        data = db.get_items(Config.QUERY_TO_VIEW_HISTORY, (self.user_id,))
        logger.info("History viewed for user_id: %s", self.user_id)
        return data

    def insert_history(self):
        """
            Function to insert history
        """
        logger.debug(Config.INSERTING_HISTORY, self.user_id)
        tm = datetime.now()
        date_time = tm.strftime(Config.FORMAT_DATE_TIME)
        searched_by = Config.CITY_NAME
        searched_for = Config.CURRENT_WEATHER
        query = Config.QUERY_TO_INSERT_SEARCH_HISTORY
        _id = db.add_item(query, (self.user_id,searched_for, searched_by, date_time, self.city))
        logger.info(Config.INSERTED_HISTORY, self.user_id)
        return _id
