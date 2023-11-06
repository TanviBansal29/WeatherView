from db.database_connection import DatabaseConnection
from config.config import Config
from tabulate import tabulate
import shortuuid


def create_user_table():
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_CREATE_USERS_TABLE)


def create_history_table():
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_CREATE_SEARCH_HISTORY_TABLE)


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


def fetch_role_and_id(username, password):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_FETCH_ROLE, (username, password)).fetchone()
        role = data[5]
        user_id = data[0]
        return (role, user_id)


def insert_history(user_id, searched_for, searched_by, date_time, city):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_INSERT_SEARCH_HISTORY, (user_id,searched_for, searched_by, date_time, city))


def fetch_user_data(username):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_VIEW_USER, (username,)).fetchall()
        if len(data) == 0:
            print(Config.NO_DATA)
        else:
            HEADERS  = ["username","city","zipcode"]
            print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def fetch_user_by_city(city):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_VIEW_USER_BY_PLACE, (city,)).fetchall()
        if len(data) == 0:
            print(Config.NO_DATA)
        else:
            HEADERS  = ["user_id","username","city","zipcode"]
            print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def view_history(user_id):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_VIEW_HISTORY, (user_id,)).fetchall()
        if len(data) == 0:
            print(Config.NO_DATA)
        else:
            HEADERS  = ["date_time", "searched_for", "searched_by", "city_name"]
            print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def fetch_all_users():
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(Config.QUERY_TO_FETCH_ALL_USERS).fetchall()
        HEADERS  = ["user_id","username","city","zipcode"]
        print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))
