from datetime import datetime
from config.config import Config
from db.database import db


class History:
    def __init__(self,user_id, city=None):
        self.user_id = user_id
        self.city = city

    def view_history(self):
        data = db.get_items(Config.QUERY_TO_VIEW_HISTORY, (self.user_id,))
        return data

    def insert_history(self):
        tm = datetime.now()
        date_time = tm.strftime(Config.FORMAT_DATE_TIME)
        searched_by = Config.CITY_NAME
        searched_for = Config.CURRENT_WEATHER
        db.add_item(Config.QUERY_TO_INSERT_SEARCH_HISTORY, (self.user_id,searched_for, searched_by, date_time, self.city))
