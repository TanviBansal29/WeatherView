from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from controller.user.user import UserController
from helpers.rbac import access_control

blp = Blueprint("User",__name__, description = "Routes for User opeartions")


@blp.route("/users/<string:username>")
class UserDetails(MethodView):
    'Route to get user details by username'

    @access_control("admin")
    def get(self, username):
        '''
            Get user details by username
            Details = {username , city, zipcode}
        '''
        user_obj = UserController(username)
        return user_obj.view_user_data()

@blp.route("/users")
class UsersList(MethodView):

    @access_control("admin")
    def get(self):
        '''
            Get details of users with specified place name
        '''
        city = request.args.get("place")
        user_obj = UserController(city=city)
        return user_obj.view_users()
    