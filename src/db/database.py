import sqlite3
from dotenv import load_dotenv
from config.config import Config
from helpers.exceptions import DbException

load_dotenv()


class Database:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def add_item(self, query, data):
        try:
            self.cursor.execute(query, data)
            _id = self.cursor.last
            self.connection.commit()

        except Exception:
            raise DbException()
        else:
            return _id

    def get_item(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchone()
        except Exception:
            raise DbException
        else:
            return response

    def get_items(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchall()
            self.connection.commit()
        except Exception:
            raise DbException
        else:
            return response

    def __del__(self):
        print("Closing....")
        self.connection.close()
        super().__del__()

db = Database(Config.DATABASE_NAME)
