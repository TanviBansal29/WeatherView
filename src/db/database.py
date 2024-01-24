import mysql.connector
from dotenv import load_dotenv
from config.config import Config
from helpers.exceptions import DbException

load_dotenv()

class Database:
    def __init__(self, file):
        self.connection = mysql.connector.connect(user='tanvi', password='123456',
                              host='127.0.0.1',
                              database='weatherdb')
        self.cursor = self.connection.cursor()
        self.cursor.execute(Config.QUERY_TO_CREATE_USERS_TABLE)
        self.cursor.execute(Config.QUERY_TO_CREATE_SEARCH_HISTORY_TABLE)

    def add_item(self, query, data):
        try:
            self.cursor.execute(query, data)
            _id = self.cursor.lastrowid
            self.connection.commit()

        except Exception:
            raise DbException()
        return _id

    def get_item(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchone()
        except Exception:
            raise DbException
        return response

    def get_items(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchall()
            self.connection.commit()
        except Exception:
            raise DbException
        return response


db = Database(Config.DATABASE_NAME)
          