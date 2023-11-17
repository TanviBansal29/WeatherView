import logging
import hashlib
from os import system
from config.config import Config
from pwinput import pwinput
from db.helper_functions import verify_username
from db.helper_functions import create_user
from db.helper_functions import password_validation
from db.helper_functions import verify_zipcode
from db.helper_functions import verify_cityname
from authentication.authentication import Authentication

# utils -> input validations, regex, logs
logger = logging.getLogger("Auth")


class MainMenu:
    @classmethod
    def start_menu(cls):
        print(Config.WELCOME_MESSAGE)
        user_option = input(Config.MENU_PROMPTS)
        while user_option != Config.QUIT:
            if user_option == Config.FIRST:
                Authentication.login()
            elif user_option == Config.SECOND:
                cls.signup()
            else:
                print(Config.INVALID_INPUT)
            user_option = input(Config.MENU_PROMPTS)
        # system('cls')

    @staticmethod
    def signup():
        username = input(Config.ENTER_USERNAME).strip()
        while len(username) == 0 or verify_username(username):
            username = input("Please enter valid username : ").strip()
        password = pwinput(Config.ENTER_PASSWORD)
        while password_validation(password):
            password = pwinput(Config.STRONG_PASSWORD_PROMPT)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        city = input(Config.ENTER_CITY).lower()
        while verify_cityname(city):
            city = input("Please enter valid city name : ").lower()
        zipcode = input(Config.ENTER_ZIPCODE)
        while verify_zipcode(zipcode):
            zipcode = input("Please enter a valid zipcode: ")
        create_user(username, hashed_password, city, zipcode)
        logger.info(f"Sucessfully signed up new user with {username}.")
