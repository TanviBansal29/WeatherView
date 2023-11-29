from tabulate import tabulate

from config.config import Config


class TableHelper:
    """
        Table Helper class to tabulate and print table
    """
    USERNAME_HEADERS = ("username", "city", "zipcode")
    CITY_HEADERS = ("user_id", "username", "city", "zipcode")
    HISTORY_HEADERS = ("date time", "searched_for", "searched_by", "city_name")
    FORECAST_HEADER = ('Date', 'Max temp', 'Min temp', 'Windspeed', 'Sunrise', 'Sunset')
    WEATHER_HEADER = ('Max temp', 'Min temp', 'Windspeed', 'Sunrise', 'Sunset')

    @staticmethod
    def print_table(data, type):
        """
            Function to print table
        """
        if type == "username":
            table_headers = TableHelper.USERNAME_HEADERS
        if type == "city":
            table_headers = TableHelper.CITY_HEADERS
        if type == "history":
            table_headers = TableHelper.HISTORY_HEADERS
        if type == "forecast":
            table_headers = TableHelper.FORECAST_HEADER
        if type == "weather":
            table_headers = TableHelper.WEATHER_HEADER

        print(tabulate(data, headers=table_headers, tablefmt=Config.TABLE_FORMAT))
