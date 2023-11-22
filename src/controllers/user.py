from tabulate import tabulate
from src.config.config import Config
from src.db.database import db
from src.helpers.table_helper import TableHelper


class User:
    def __init__(self, username):
        self.username = username
        
    def fetch_user_data(username):
        data = db.get_items(Config.QUERY_TO_VIEW_USER, (username,))
        return data
        
    def fetch_user_by_city(city):
        data = db.get_items(Config.QUERY_TO_VIEW_USER_BY_PLACE, (city,))
        return data

    def fetch_all_users():
        data = db.get_items(Config.QUERY_TO_FETCH_ALL_USERS)
        TableHelper.print_table(data, type = "city")
