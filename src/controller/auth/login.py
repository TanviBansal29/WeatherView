from typing import Dict
from flask_smorest import abort
from flask_jwt_extended import create_access_token, create_refresh_token 
from helpers.custom_exceptions import InvalidCredentials
from business.authentication import Authentication

class LoginController:
    '''
    LoginController class with Login method
    '''
    def __init__(self,login_data):
        self.username = login_data['username']
        self.password = login_data['password']
        self.obj_authentication_business = Authentication(self.username,self.password)

    def login(self): 
        '''Method for user login'''
        try:
            # username, password = user_data.values()
            result = self.obj_authentication_business.verify_user()

            if result:
                data = self.obj_authentication_business.get_role()
                role = data["role"]
                user_id = data["user_id"]
                token = self.obj_authentication_business.generate_token(role, user_id)

                response = {
                    "access_token": token["access_token"],
                    "refresh_token": token["refresh_token"],
                    "message": "LOGGED IN SUCCESSFULLY"
                }

                return response
        except InvalidCredentials:
            abort(401, "Invalid user credentials were provided")





        

    