# get user
# post user
from flask_smorest import Blueprint

blp = Blueprint("User",__name__, description = "Routes for User opeartions")


@blp.route("/users/<string:username>")
class UserDetails(MethodView):
    'Route to get user details'

    def get():
        '''
            Get user details by username
            Details = {username , city, zipcode}
        '''
        
        pass



