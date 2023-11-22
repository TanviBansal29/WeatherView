import re
from src.config.config import Config

class Validator:
    @staticmethod
    def validate_password(password):
        reg = Config.PASSWORD_REGEX
        pat = re.compile(reg)
        mat = re.search(pat,password)
        return mat

    @staticmethod
    def validate_zipcode(zipcode):
        reg = Config.ZIPCODE_REGEX
        pat = re.compile(reg)
        mat = re.search(pat,zipcode)
        return mat

    @staticmethod
    def validate_cityname(city):
        reg = Config.CITY_REGEX 
        pat = re.compile(reg)
        mat = re.search(pat, city)
        return mat
    
    @staticmethod
    def validate_username(username):
        reg = Config.USERNAME_REGEX 
        pat = re.compile(reg)
        mat = re.search(pat, username)
        return mat