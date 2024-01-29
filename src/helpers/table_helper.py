from tabulate import tabulate as tb

from config.config import Config


class TableHelper:
    """
        Table Helper class to tabulate and print table
    """
    USERNAME_HEADERS = Config.USERNAME_HEADERS
    CITY_HEADERS = Config.CITY_HEADERS
    HISTORY_HEADERS = Config.HISTORY_HEADER
    FORECAST_HEADER = Config.FORECAST_HEADER
    WEATHER_HEADER = Config.WEATHER_HEADER

    @staticmethod
    def print_table(data, type):
        """
            Function to print table
        """

        if type == Config.TYPE_USERNAME:
            table_headers = TableHelper.USERNAME_HEADERS
        if type == Config.TYPE_CITY:
            table_headers = TableHelper.CITY_HEADERS
        if type == Config.TYPE_HISTORY:
            table_headers = TableHelper.HISTORY_HEADERS
        if type == Config.TYPE_FORECAST:
            table_headers = TableHelper.FORECAST_HEADER
        if type == Config.TYPE_WEATHER:
            table_headers = TableHelper.WEATHER_HEADER

        print(tb(data, headers=table_headers, tablefmt=Config.TABLE_FORMAT))
