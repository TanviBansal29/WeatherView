import hashlib
from config.config import Config
from pwinput import pwinput
from db.helper_functions import verify_username
from db.helper_functions import create_user
from authentication.authentication import Authentication

# utils -> input validations, regex, logs

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

    @staticmethod
    def signup():
        while True:
            username = input(Config.ENTER_USERNAME)
            if verify_username(username):
                continue
            else:
                password = pwinput(Config.ENTER_PASSWORD)
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                city = input(Config.ENTER_CITY)
                zipcode = int(input(Config.ENTER_ZIPCODE))
                create_user(username, hashed_password, city, zipcode)
                break









