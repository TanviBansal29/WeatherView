import mysql.connector
import os
import logging
from config.config import Config
from helpers import DbException

logger = logging.getLogger("Database")


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(Config.QUERY_TO_CREATE_USERS_TABLE)
        self.cursor.execute(Config.QUERY_TO_CREATE_SEARCH_HISTORY_TABLE)

    def add_item(self, query, data):
        try:
            self.cursor.execute(query, data)
            _id = self.cursor.lastrowid
            self.connection.commit()

        except Exception as e:
            raise DbException(f"Couldn't add data {e}")

        return _id

    def get_item(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchone()

        except Exception as e:
            raise DbException(f"Couldn't get data {e}")

        return response

    def get_items(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchall()
            self.connection.commit()

        except Exception as e:
            raise DbException(f"Couldn't get data(many) {e}")

        return response


try:
    db = Database()
except Exception as e:
    raise DbException(f"Couldn't connect to database {e}")
