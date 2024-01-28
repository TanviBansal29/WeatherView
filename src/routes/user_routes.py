from flask.views import MethodView
from flask_smorest import Blueprint
from controller.user import UserController

blp = Blueprint("User",__name__, description = "Routes for User opeartions")


@blp.route("/users/<string:username>")
class UserDetails(MethodView):
    'Route to get user details'

    def get(self):
        '''
            Get user details by username
            Details = {username , city, zipcode}
        '''
        user_obj = UserController()
        return user_obj.view_user_data()


