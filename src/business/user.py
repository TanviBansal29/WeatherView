import logging
from config.config import Config
from db.database import db
from helpers import DataNotFound

logger = logging.getLogger(__name__)


class User:
    def __init__(self, username=None, city=None):
        self.username = username
        self.city = city

    def fetch_user_data(self):
        """Function to fetch user data"""

        logger.info("Fetching user data by user name")

        data = db.get_items(Config.QUERY_TO_VIEW_USER, (self.username,))
        if not data:
            raise DataNotFound(Config.NO_DATA)
        print(data)
        response = {"username": data[0][0], "city": data[0][1], "zipcode": data[0][2]}
        return response

    def fetch_user_by_city(self):
        """Function to fetch user data by city name"""

        logger.info("Fetching user data by city name")

        data = db.get_items(Config.QUERY_TO_VIEW_USER_BY_PLACE, (self.city,))
        if not data:
            raise DataNotFound(Config.NO_DATA)
        user_data = []
        for item in data:
            response = {
                "user_id": item[0],
                "username": item[1],
                "city": item[2],
                "zipcode": item[3],
            }
            user_data.append(response)
        return user_data
