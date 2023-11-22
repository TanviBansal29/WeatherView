import hashlib
import logging
from os import system
from config.config import Config
from pwinput import pwinput
from controllers.history import History
from controllers.user import User
from controllers.weather import Weather
from helpers.table_helper import TableHelper
from helpers.validations import Validator
from controllers.authentication import Authentication
from utils.pretty_print import get_table

logger = logging.getLogger("Auth")

class MainMenu:
    @classmethod
    def start_menu(cls):
        print(Config.WELCOME_MESSAGE)
        user_option = input(Config.MENU_PROMPTS)

        while user_option != Config.QUIT:
            if user_option == Config.FIRST:
                MainMenu.__login_helper()

            elif user_option == Config.SECOND:
                MainMenu.__signup_helper()

            else:
                print(Config.INVALID_INPUT)
                
            user_option = input(Config.MENU_PROMPTS)
        # system('cls')

    @staticmethod
    def __login_helper():
        while True:
            username = input(Config.ENTER_USERNAME)
            password = pwinput(Config.ENTER_PASSWORD).strip()
            auth = Authentication(username, password)
            isUserValid = auth.verify_user()
            if isUserValid:
                break
            print(Config.INVALID_CREDENTIALS)
        role, user_id = auth.get_role()
        if role == Config.ADMIN:
            adminhelper_obj = AdminHelper()
            adminhelper_obj.admin_controller()
        else:
            userhelper_obj  = UserHelper(user_id)
            userhelper_obj.user_controller()

    @staticmethod
    def __signup_helper():
        username = MainMenu.__username_helper()
        hashed_password = MainMenu.__get_password()
        city = MainMenu.__get_cityname()
        zipcode = MainMenu.__get_zipcode()
        auth = Authentication(username, hashed_password, city, zipcode)
        auth.create_account()
        print(Config.SIGNUP_PRMOMPT)

    @staticmethod
    def __username_helper():
        username = MainMenu.__get_username()
        auth = Authentication(username)
        while not auth.verify_username():
            print(Config.USERNAME_ERROR)
            username = MainMenu.__get_username()
        return username
    
    @staticmethod
    def __get_username():
        username = input(Config.ENTER_USERNAME).strip()
        while not Validator.validate_username(username):
            username = input("Please enter valid username : ").strip()
        return username

    @staticmethod
    def __get_password():
        password = pwinput(Config.ENTER_PASSWORD)
        while not Validator.validate_password(password):
            password = pwinput(Config.STRONG_PASSWORD_PROMPT)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    @staticmethod
    def __get_cityname():
        city = input(Config.ENTER_CITY).lower()
        while not Validator.validate_cityname(city):
            city = input("Please enter valid city name : ").lower()
        return city
    
    @staticmethod
    def __get_zipcode():
        zipcode = input(Config.ENTER_ZIPCODE)
        while not Validator.validate_zipcode(zipcode):
            zipcode = input("Please enter a valid zipcode: ")
        return zipcode
    

class AdminHelper:
    def admin_controller(self):
        print(Config.LOGIN_ADMIN)
        admin_choice = input(Config.ADMIN_PROMPTS)
        while admin_choice != Config.QUIT:
            if admin_choice == Config.FIRST:
                self.__get_user_data_helper()

            elif admin_choice == Config.SECOND:
                self.__get_user_by_city_helper()

            elif admin_choice == Config.THIRD:
                self.__get_user_history_helper()

            else:
                print(Config.INVALID_INPUT)
            admin_choice = input(Config.ADMIN_PROMPTS)

    def __get_user_data_helper(self):
        data = self.__get_user_data()
        if data:
            TableHelper.print_table(data, type = "username")
        else:
            print(Config.NO_DATA)

    def __get_user_data(self):
        username = input(Config.ENTER_USERNAME)
        data = User.fetch_user_data(username)
        return data
    
    def __get_user_by_city_helper(self):
        User.fetch_all_users()
        data = self.__get_user_by_city()
        if data:
            TableHelper.print_table(data, type = "city")      
        else:
            print(Config.NO_DATA)

    def __get_user_history_helper(self):
        User.fetch_all_users()
        data = self.__get_user_history()
        print(data)

    def __get_user_by_city(self):
        city = input(Config.ENTER_CITYNAME).lower()
        data = User.fetch_user_by_city(city)
        return data
    
    def __get_user_history(self):
        user_id = input(Config.ENTER_USERID)
        history_obj = History(user_id)
        data = history_obj.view_history()
        return data


class UserHelper:
    def __init__(self, user_id):
        self.user_id = user_id

    def user_controller(self):
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

    def __get_weather_data(self):
        user_choice = input(Config.USER_PROMPTS)
        while user_choice != Config.QUIT:
            if user_choice == Config.FIRST:
                self.__get_weather_data_by_city_helper()
                break

            elif user_choice == Config.SECOND:
                self.__get_weather_data_by_coordinates_helper()
                break
            else:
                print(Config.INVALID_INPUT)
            user_choice = input(Config.USER_PROMPTS)

    def __get_weather_data_by_city_helper(self):
        city_name = input(Config.ENTER_CITYNAME)
        weather_obj = Weather(city_name = city_name)
        data = weather_obj.get_weather_by_city()
        if data:
            print(get_table(data))
        history_obj = History(self.user_id, city_name)
        history_obj.insert_history()
     

    def __get_weather_forecast(self):
        city_name = input(Config.ENTER_CITYNAME)
        weather_obj = Weather(city_name = city_name)
        data = weather_obj.get_forecast()
        if data:
            TableHelper.print_table(data, type = "forecast")
            history_obj = History(self.user_id, city_name)
            history_obj.insert_history()
        else:
            print(Config.NO_DATA)

    def __get_history(self):
        history_obj = History(self.user_id)
        data = history_obj.view_history()
        if data:
            TableHelper.print_table(data, type = "history")
        else:
            print(Config.NO_DATA)

    def __get_weather_data_by_coordinates_helper(self):
        lat = float(input(Config.LATITUDE))
        lon = input(Config.LONGITUDE)
        weather_obj = Weather(lat = lat, lon = lon)
        weather_obj.get_weather_by_cordinates()
        history_obj = History(self.user_id,"-")
        history_obj.insert_history()