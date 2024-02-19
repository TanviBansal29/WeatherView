import os
import pymysql
import logging
from config.config import Config
from helpers import DbException

logger = logging.getLogger("Database")


class Database:
    def __init__(self):
        timeout = 10
        self.connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db="defaultdb",
            host="mysql-1adcb7fa-bansaltanvi2404-b909.a.aivencloud.com",
            password="AVNS_969BhvbhbIu9KWqHfDk",
            read_timeout=timeout,
            port=17131,
            user="avnadmin",
            write_timeout=timeout,
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
