import hashlib
import logging
import os
from pwinput import pwinput
from config.config import Config
from handler.authentication import Authentication
from helpers.validations import Validator
from views.admin_view import AdminHelper
from views.user_view import UserHelper

logger = logging.getLogger(__name__)


class MainMenu:
    """
        Provides login and signup view.
    """

    @staticmethod
    def start_menu():
        """
            Function to display user prompts
        """
        os.system('cls')
        print(Config.WELCOME_MESSAGE)

        logger.debug(Config.START_MENU)
        
        user_option = input(Config.MENU_PROMPTS)

        while user_option != Config.QUIT:
            if user_option == Config.FIRST:
                MainMenu.__login_helper()

            elif user_option == Config.SECOND:
                MainMenu.__signup_helper()

            else:
                print(Config.INVALID_INPUT)

            user_option = input(Config.MENU_PROMPTS)

    @staticmethod
    def __login_helper():
        """
            Function to verify input username and password
        """
        os.system('cls')
        logger.debug(Config.LOGIN_INPUTS)
        while True:
            username = input(Config.ENTER_USERNAME)
            password = pwinput(Config.ENTER_PASSWORD).strip()
            auth = Authentication(username, password)
            is_user_valid = auth.verify_user()
            if is_user_valid:
                break
            print(Config.INVALID_CREDENTIALS)
        role = auth.get_role().get(Config.ROLE)
        user_id = auth.get_role().get(Config.USER_ID)
        if role == Config.ADMIN:
            adminhelper_obj = AdminHelper()
            adminhelper_obj.admin_controller()
        else:
            userhelper_obj = UserHelper(user_id)
            userhelper_obj.user_controller()

    @staticmethod
    def __signup_helper():
        """
            Private helper function to call username and password helpers
        """
        os.system('cls')
        logger.debug(Config.SIGNIN_INPUTS)
        username = MainMenu.__username_helper()
        hashed_password = MainMenu.__get_password()
        city = MainMenu.__get_cityname()
        zipcode = MainMenu.__get_zipcode()
        auth = Authentication(username, hashed_password, city, zipcode)
        auth.create_account()
        print(Config.SIGNUP_PROMPT)

    @staticmethod
    def __username_helper():
        """
            Private helper function to get username and verify it
        """
        logger.debug(Config.VERIFY_USERNAME)
        username = MainMenu.__get_username()
        auth = Authentication(username)
        while not auth.verify_username():
            print(Config.USERNAME_ERROR)
            username = MainMenu.__get_username()
        return username

    @staticmethod
    def __get_username():
        """
            Function to check if username is unique or not
        """
        logger.debug(Config.GET_USERNAME)
        username = input(Config.ENTER_USERNAME).strip()
        while not Validator.validate_username(username):
            username = input(Config.VALID_USERNAME).strip()
        return username

    @staticmethod
    def __get_password():
        """
            Function to input password
        """
        logger.debug(Config.GET_PASSWORD)
        password = pwinput(Config.ENTER_PASSWORD)
        while not Validator.validate_password(password):
            password = pwinput(Config.STRONG_PASSWORD_PROMPT)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    @staticmethod
    def __get_cityname():
        """
            Function to input cityname
        """
        logger.debug(Config.GET_CITYNAME)
        city = input(Config.ENTER_CITY).lower()
        while not Validator.validate_cityname(city):
            city = input(Config.INVALID_CITYNAME).lower()
        return city

    @staticmethod
    def __get_zipcode():
        """
            Function to get zipcode
        """
        logger.debug(Config.GET_ZIPCODE_START)
        zipcode = input(Config.ENTER_ZIPCODE)
        while not Validator.validate_zipcode(zipcode):
            zipcode = input(Config.INVALID_ZIPCODE)
        return zipcode
