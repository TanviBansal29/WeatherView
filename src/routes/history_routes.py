# get history
from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from controller.history.history import HistoryController

from flask_smorest import Blueprint

from helpers.rbac import access_control

blp = Blueprint("History",__name__, description="Routes for getting user search history")


@blp.route("/history")
class UserHistory(MethodView):
    'Route to get user search history'

    @access_control("admin")
    def get(self):
        '''
            Get user search history by user id
        '''
        user_id = request.args.get("user_id")
        history_obj = HistoryController(user_id)
        return history_obj.view_user_history()


class UserHistoryMe(MethodView):
    'Route to get logged in user search history'

    @access_control("user")
    def get(self):
        '''
            Get own search history
        '''
        claims = get_jwt()
        user_id = claims.get("sub")
        history_obj = HistoryController(user_id)
        return history_obj.view_user_history()
    