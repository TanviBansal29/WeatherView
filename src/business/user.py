from config.config import Config
from db.database import db
from helpers import DataNotFound


class User:
    def __init__(self, username=None, city=None):
        self.username = username
        self.city = city

    def fetch_user_data(self):
        data = db.get_items(Config.QUERY_TO_VIEW_USER, (self.username,))
        if not data:
            raise DataNotFound("No data found")
        return data

    def fetch_user_by_city(self):
        data = db.get_items(Config.QUERY_TO_VIEW_USER_BY_PLACE, (self.city,))
        print(data)
        if not data:
            raise DataNotFound("No data found")
        return data

    # @staticmethod
    # def fetch_all_users():
    #     data = db.get_items(Config.QUERY_TO_FETCH_ALL_USERS)
    #     TableHelper.print_table(data, type="city")
