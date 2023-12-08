import os
from config.config import Config
from controllers.history import History
from controllers.weather import Weather
from helpers.table_helper import TableHelper


class UserHelper:
    """
        Class for user controllers
    """
    def __init__(self, user_id):
        self.user_id = user_id

    def user_controller(self):
        """
            Function to display user view prompts
        """
        os.system('cls')
        print(Config.LOGIN_USER)
        user_input = input(Config.USER_VIEW_PROMPTS)
        while user_input != Config.QUIT:
            if user_input == Config.FIRST:
                self.__get_weather_data()

            elif user_input == Config.SECOND:
                self.__get_weather_forecast()

            elif user_input == Config.THIRD:
                self.__get_history()

            else:
                print(Config.INVALID_INPUT)

            user_input = input(Config.USER_VIEW_PROMPTS)
            os.system('cls')

    def __get_weather_data(self):
        """
            Function to select weather data or forecast
        """
        user_choice = input(Config.USER_PROMPTS)
        while user_choice != Config.QUIT:
            if user_choice == Config.FIRST:
                self.__get_weather_data_by_city_helper()
                break
            if user_choice == Config.SECOND:
                self.__get_weather_data_by_coordinates_helper()
                break
            print(Config.INVALID_INPUT)
            user_choice = input(Config.USER_PROMPTS)

    def __get_weather_data_by_city_helper(self):
        """
            Function to input cityname and get weather by city
        """
        city_name = input(Config.ENTER_CITYNAME)
        weather_obj = Weather(city_name=city_name)
        data = weather_obj.get_weather_by_city()
        if data:
            TableHelper.print_table([data], type="weather")
            history_obj = History(self.user_id, city_name)
            history_obj.insert_history()
        else:
            print(Config.NO_DATA)

    def __get_weather_forecast(self):
        """
            Function to input cityname and get forecast data
        """
        city_name = input(Config.ENTER_CITYNAME)
        weather_obj = Weather(city_name=city_name)
        days = int(input(Config.ENTER_DAYS))
        data = weather_obj.get_forecast(days)
        if data:
            TableHelper.print_table(data, type="forecast")
            history_obj = History(self.user_id, city_name)
            history_obj.insert_history()
        else:
            print(Config.NO_DATA)

    def __get_history(self):
        """
            Function to view user history
        """
        history_obj = History(self.user_id)
        data = history_obj.view_history()
        if data:
            TableHelper.print_table(data, type="history")
        else:
            print(Config.NO_DATA)

    def __get_weather_data_by_coordinates_helper(self):
        """
            Function to get weather data by latitude and longitude
        """
        lat = float(input(Config.LATITUDE))
        lon = input(Config.LONGITUDE)
        weather_obj = Weather(lat=lat, lon=lon)
        data = weather_obj.get_weather_by_coordinates()
        if data:
            TableHelper.print_table([data], type="weather")
            history_obj = History(self.user_id, "-")
            history_obj.insert_history()
        else:
            print(Config.NO_DATA)
