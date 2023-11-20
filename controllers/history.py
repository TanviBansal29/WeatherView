from datetime import datetime
from tabulate import tabulate
from config.config import Config
from db.database import db


class History:
    def view_history(user_id):
        data = db.get_items(Config.QUERY_TO_VIEW_HISTORY, (user_id,))
        return data

    def insert_history(user_id,city):
        tm = datetime.now()
        date_time = tm.strftime(Config.FORMAT_DATE_TIME)
        searched_by = Config.CITY_NAME
        searched_for = Config.CURRENT_WEATHER
        db.add_item(Config.QUERY_TO_INSERT_SEARCH_HISTORY, (user_id,searched_for, searched_by, date_time, city))
