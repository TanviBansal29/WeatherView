import logging
import hashlib
import shortuuid
from db.database import db
from config.config import Config

logger = logging.getLogger('Logging')


class Authentication:

    def __init__(self, username, password=None, city=None, zipcode=None):
        self.username = username
        self.password = password
        self.city = city
        self.zipcode = zipcode

    def get_role(self):
        logger.info(f"Logged in succesfully with {self.username}")
        role_dict = self.__fetch_role_and_id()
        return role_dict

    def verify_user(self):
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        data = db.get_item(Config.QUERY_TO_VERIFY_USER, (self.username, hashed_password))
        if not data:
            return False
        return True

    def __fetch_role_and_id(self):
        data = db.get_item(Config.QUERY_TO_FETCH_ROLE, (self.username,))
        if data:
            role = data[1]
            user_id = data[0]
            return {"role" : role, "user_id":user_id}
 
    def verify_username(self):
        data = db.get_item(Config.QUERY_TO_VERIFY_USERNAME, (self.username,))
        if data:
            return False
        return True

    def create_account(self):
        user_id = shortuuid.ShortUUID().random(length=5)
        _id = db.add_item(Config.QUERY_TO_CREATE_USER, (user_id, self.username, self.password, self.city, self.zipcode))
        logger.info(f"Sucessfully signed up new user with {self.username}.")
        return _id
