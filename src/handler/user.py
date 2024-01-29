import logging
from config.config import Config
from db.database import db
from helpers.table_helper import TableHelper

logger = logging.getLogger(__name__)

class User:
    def __init__(self, username=None, city=None):
        self.username = username
        self.city = city

    def fetch_user_data(self):
        logger.debug(Config.FETCH_USER_DATA, self.username)
        data = db.get_items(Config.QUERY_TO_VIEW_USER, (self.username,))
        return data

    def fetch_user_by_city(self):
        logger.debug(Config.FETCH_USER_DATA_IN_CITY, self.city)
        data = db.get_items(Config.QUERY_TO_VIEW_USER_BY_PLACE, (self.city,))
        return data

    @staticmethod
    def fetch_all_users():
        logger.debug(Config.FETCH_ALL_USER)
        data = db.get_items(Config.QUERY_TO_FETCH_ALL_USERS)
        TableHelper.print_table(data, type=Config.TYPE_CITY)
        logger.info(Config.USERS_SUCCESS_LOG)
