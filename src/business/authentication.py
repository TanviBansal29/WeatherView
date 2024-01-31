import logging
import hashlib
import shortuuid
from db.database import db
from config.config import Config
from helpers.blocklist import BLOCKLIST
from flask_jwt_extended import create_access_token, create_refresh_token
from helpers.custom_exceptions import DataAlreadyExists, DataNotFound


logger = logging.getLogger('Logging')

class Authentication:
    """
        Class for authentication
    """
    def __init__(self, username=None, password=None, city=None, zipcode=None):
        self.username = username
        self.password = password
        self.city = city
        self.zipcode = zipcode

    def get_role(self):
        """
            Function to get user role
        """
        logger.info("Logged in succesfully with %s", self.username)
        role_dict = self.__fetch_role_and_id()
        return role_dict

    def verify_user(self):
        """
            Function to verify user
        """
        logger.debug('Verifying username')
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        data = db.get_item(Config.QUERY_TO_VERIFY_USER, (self.username, hashed_password))
        return data
        # if not data:
        #     return False
        # return True

    def __fetch_role_and_id(self):
        """
            Function to fetch role and user_id
        """
        logger.debug('Fetching role and user_id')
        data = db.get_item(Config.QUERY_TO_FETCH_ROLE, (self.username,))
        # return data
        if data:
            role = data[1]
            user_id = data[0]
            return {"role" : role, "user_id":user_id}
 
    def verify_username(self):
        """
            Function to verify username
        """
        logger.debug('Verifying username')
        data = db.get_item(Config.QUERY_TO_VERIFY_USERNAME, (self.username,))
        if data:
            raise DataAlreadyExists("Enter new username")
        return 

    def create_account(self):
        """
            Function to create user account
        """
        logger.debug('Creating account')
        user_id = shortuuid.ShortUUID().random(length=5)
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        _id = db.add_item(Config.QUERY_TO_CREATE_USER, (user_id, self.username, hashed_password, self.city, self.zipcode))
        logger.info("Sucessfully signed up new user with %s." , self.username)
        return _id
    
    def generate_token(self,role,user_id):
        'Method to generate access token and refresh token'

        access_token = create_access_token(identity=user_id, fresh = True,additional_claims={"role": role})
        refresh_token = create_refresh_token(identity = user_id,additional_claims= {"role" : role} )
        return {"access_token": access_token, "refresh_token": refresh_token}
    
    def refresh(self,user_id, role):
        'Method to generate refresh token'

        new_access_token = create_access_token(
            identity = user_id,
            fresh = False,
            additional_claims = {"role": role}
            )
        return new_access_token

    def logout(self, token_id):
        '''Method to logout an authenticated user'''

        BLOCKLIST.add(token_id)
