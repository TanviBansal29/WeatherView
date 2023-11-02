from config.config import Config
from pwinput import pwinput
from db.helper_functions import verify_username
from db.helper_functions import create_user
from db.helper_functions import verify_user
from db.helper_functions import fetch_role
from authentication import Authentication

# utils -> input validations, regex, logs

class MainMenu:
    @classmethod
    def start_menu(cls):
        print(Config.WELCOME_MESSAGE)
        user_option = input(Config.MENU_PROMPTS)
        while user_option != 'q':
            if user_option == '1':
                Authentication.login()
            elif user_option == '2':
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
                city = input(Config.ENTER_CITY)
                zipcode = int(input(Config.ENTER_ZIPCODE))
                create_user(username, password, city, zipcode)
                break









