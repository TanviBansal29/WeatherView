from tabulate import tabulate

from config.config import Config


class TableHelper:
    USERNAME_HEADERS = ("username", "city", "zipcode")
    CITY_HEADERS = ("user_id", "username", "city", "zipcode")
    HISTORY_HEADERS = ("date time", "searched_for", "searched_by", "city_name")
    FORECAST_HEADER = ('Date', 'Max temp', 'Min temp', 'Windspeed', 'Rain', 'Sunrise', 'Sunset')

    @staticmethod
    def print_table(data, type):
        if type == "username":
            HEADERS = TableHelper.USERNAME_HEADERS
        if type == "city":
            HEADERS = TableHelper.CITY_HEADERS
        if type == "history":
            HEADERS = TableHelper.HISTORY_HEADERS
        if type == "forecast":
            HEADERS = TableHelper.FORECAST_HEADER

        print(tabulate(data, headers=HEADERS, tablefmt=Config.TABLE_FORMAT))
