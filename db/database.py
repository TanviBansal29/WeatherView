import sqlite3
from config.config import Config
from helpers.exceptions import DbException
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def add_item(self, query, data):
        try:
            self.cursor.execute(query, data)
            self.connection.commit()

        except Exception:
            raise DbException()

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

db = Database(Config.DATABASE_NAME)