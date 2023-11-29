import re
from config.config import Config


class Validator:
    """
        Validator class
    """

    @staticmethod
    def validate_password(password):
        """
            Function to validate password
        """
        reg = Config.PASSWORD_REGEX
        pat = re.compile(reg)
        mat = re.search(pat, password)
        return mat

    @staticmethod
    def validate_zipcode(zipcode):
        """
            Function to validate zipcode
        """
        reg = Config.ZIPCODE_REGEX
        pat = re.compile(reg)
        mat = re.search(pat, zipcode)
        return mat

    @staticmethod
    def validate_cityname(city):
        """
            Function to validate cityname
        """
        reg = Config.CITY_REGEX
        pat = re.compile(reg)
        mat = re.search(pat, city)
        return mat

    @staticmethod
    def validate_username(username):
        """
            Function to validate username
        """
        reg = Config.USERNAME_REGEX
        pat = re.compile(reg)
        mat = re.search(pat, username)
        return mat
