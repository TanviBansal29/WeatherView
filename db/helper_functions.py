from db.database import db
from config.config import Config
from tabulate import tabulate
import re

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


def fetch_all_users():
    data = db.get_items(Config.QUERY_TO_FETCH_ALL_USERS)
    HEADERS  = ["user_id","username","city","zipcode"]
    print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))

        




