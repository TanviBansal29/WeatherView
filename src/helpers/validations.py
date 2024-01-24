import re
from config.config import Config


class Validator:
    """
        Validator class
    """

    @staticmethod
    def validate(reg, user_input):
        pat = re.compile(reg)
        mat = re.search(pat, user_input)
        return mat

    @staticmethod
    def validate_password(password):
        """
            Function to validate password
        """
        reg = Config.PASSWORD_REGEX
        return Validator.validate(reg, password)

    @staticmethod
    def validate_zipcode(zipcode):
        """
            Function to validate zipcode
        """
        reg = Config.ZIPCODE_REGEX
        return Validator.validate(reg, zipcode)

    @staticmethod
    def validate_cityname(city):
        """
            Function to validate cityname
        """
        reg = Config.CITY_REGEX
        return Validator.validate(reg, city)

    @staticmethod
    def validate_username(username):
        """
            Function to validate username
        """
        reg = Config.USERNAME_REGEX
        return Validator.validate(reg, username)
