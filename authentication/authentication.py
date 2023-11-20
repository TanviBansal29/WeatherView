import logging
import hashlib
import shortuuid
from db.database import db
from config.config import Config

logger = logging.getLogger('Logging')

class Authentication:
    @staticmethod
    def get_role(username):
        logger.info(f"Logged in succesfully with {username}")
        role, user_id = Authentication.__fetch_role_and_id(username)
        return role, user_id

    @staticmethod
    def verify_user(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        data = db.get_item(Config.QUERY_TO_VERIFY_USER, (username,hashed_password))
        if not data:
            return False
        return True
    
    @staticmethod
    def create_account(username, password, city, zipcode):
        user_id = shortuuid.ShortUUID().random(length=5)
        db.add_item(Config.QUERY_TO_CREATE_USER,(user_id, username, password, city, zipcode))
        logger.info(f"Sucessfully signed up new user with {username}.")
    
    @staticmethod
    def __fetch_role_and_id(username):
        data = db.get_item(Config.QUERY_TO_FETCH_ROLE, (username,))
        role = data[5]
        user_id = data[0]
        return (role, user_id)

    @staticmethod
    def verify_username(username):
        data = db.get_item(Config.QUERY_TO_VERIFY_USERNAME, (username,))
        if data:
            print(Config.USERNAME_ERROR)
            return False
        return True
    
