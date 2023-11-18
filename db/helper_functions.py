from db.database_connection import DatabaseConnection
from db.database import db
from config.config import Config
from tabulate import tabulate
import shortuuid
import re


def create_user_table():
    db.get_item(Config.QUERY_TO_CREATE_USERS_TABLE)


def create_history_table():
    db.get_item(Config.QUERY_TO_CREATE_SEARCH_HISTORY_TABLE)


def verify_username(username):
    data = db.get_item(Config.QUERY_TO_VERIFY_USERNAME, (username,))
    if data:
        print(Config.USERNAME_ERROR)
        return True
    return False


def create_user(username, password, city, zipcode):
    user_id = shortuuid.ShortUUID().random(length=5)
    db.add_items(Config.QUERY_TO_CREATE_USER,(user_id, username, password, city, zipcode))    


def verify_user(username, password):
    data = db.get_item(Config.QUERY_TO_FETCH_ROLE, (username, password))
    if not data:
        print(Config.INVALID_CREDENTIALS)
        return False
    return True


def fetch_role_and_id(username, password):
    data = db.get_item(Config.QUERY_TO_FETCH_ROLE, (username, password))
    role = data[5]
    user_id = data[0]
    return (role, user_id)


def insert_history(user_id, searched_for, searched_by, date_time, city):
    db.add_items(Config.QUERY_TO_INSERT_SEARCH_HISTORY, (user_id,searched_for, searched_by, date_time, city))


def fetch_user_data(username):
    data = db.get_items(Config.QUERY_TO_VIEW_USER, (username,))
    if len(data) == 0:
        print(Config.NO_DATA)
    else:
        HEADERS  = ["username","city","zipcode"]
        print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def fetch_user_by_city(city):
    data = db.get_items(Config.QUERY_TO_VIEW_USER_BY_PLACE, (city,))
    if len(data) == 0:
        print(Config.NO_DATA)
    else:
        HEADERS  = ["user_id","username","city","zipcode"]
        print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def view_history(user_id):
    data = db.get_items(Config.QUERY_TO_VIEW_HISTORY, (user_id,))
    if len(data) == 0:
        print(Config.NO_DATA)
    else:
        HEADERS  = ["date time", "searched_for", "searched_by", "city_name"]
        print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def fetch_all_users():
    data = db.get_items(Config.QUERY_TO_FETCH_ALL_USERS)
    HEADERS  = ["user_id","username","city","zipcode"]
    print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))


def password_validation(password):
    reg = Config.PASSWORD_REGEX
    pat = re.compile(reg)
    mat = re.search(pat,password)
    if not mat:
        return True
    return False


def verify_zipcode(zipcode):
    reg = Config.ZIPCODE_REGEX
    pat = re.compile(reg)
    mat = re.search(pat,zipcode)
    if not mat:
        return True
    return False


def verify_cityname(city):
    reg = Config.CITY_REGEX 
    pat = re.compile(reg)
    mat = re.search(pat, city)
    if not mat:
        return True
    return False

        




