import hashlib
import logging
from os import system
from config.config import Config
from pwinput import pwinput
from helpers.validations import Validator
from users.admin import admin_controller
from users.users import user_controller
from authentication.authentication import Authentication


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
            isUserValid = Authentication.verify_user(username, password)
            if isUserValid:
                break
            print(Config.INVALID_CREDENTIALS)
        role, user_id = Authentication.get_role(username)
        if role == Config.ADMIN:
            admin_controller()
        else:
            user_controller(user_id)

    @staticmethod
    def __signup_helper():
        username = MainMenu.__username_helper()
        hashed_password = MainMenu.__get_password()
        city = MainMenu.__get_cityname()
        zipcode = MainMenu.__get_zipcode()
        Authentication.create_account(username, hashed_password, city, zipcode)
        print(Config.SIGNUP_PRMOMPT)

    @staticmethod
    def __username_helper():
        username = MainMenu.__get_username()
        while not Authentication.verify_username(username):
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
    