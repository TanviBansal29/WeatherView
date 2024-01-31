from business.user import User
from helpers.custom_exceptions import DataNotFound


class UserController:
    'User Controller with user methods'

    def __init__(self, username=None, city=None):
        self.username = username
        self.city = city
        self.obj_user_business = User(username= self.username, city = self.city)

    def view_user_data(self):
        ''' Returns user data'''
        try:
            data = self.obj_user_business.fetch_user_data()
            return data
        except DataNotFound as e:
            return {"status" : 404 , "message": str(e)},404
        

    def view_users(self):
        '''
            Return list of uses with specified place name
        '''
        try:
            data = self.obj_user_business.fetch_user_by_city()
            return data
        except DataNotFound as e:
            return {"status" : 404 , "message": str(e)},404