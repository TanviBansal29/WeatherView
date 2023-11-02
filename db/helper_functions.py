from db.database_connection import DatabaseConnection
from config.config import Config
import shortuuid



def create_user_table():
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_CREATE_USERS_TABLE)

def verify_username(username):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        row = cursor.execute(Config.QUERY_TO_VERIFY_USERNAME, (username,)).fetchone()
        if row is not None:
            print(Config.USERNAME_ERROR)
            return True
        return False


def create_user(username, password, city, zipcode):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        user_id = shortuuid.ShortUUID().random(length=5)
        cursor.execute(Config.QUERY_TO_CREATE_USER,(user_id, username, password, city, zipcode))

def verify_user(username, password):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_VERIFY_USER, (username, password)).fetchone()
        if data is None:
            print(Config.INVALID_CREDENTIALS)
            return False
        return True
    

def fetch_role(username, password):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_FETCH_ROLE, (username, password)).fetchone()
        role = data[5]
        return role
