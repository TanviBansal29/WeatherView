from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt
from flask_smorest import Blueprint
from config.config import Config
from config.constants import AUTHORIZATION_HEADER
from controller.history.history import HistoryController
from flask_smorest import Blueprint
from helpers import access_control

blp = Blueprint(
    "History", __name__, description="Routes for getting user search history"
)


@blp.route("/history")
class UserHistory(MethodView):
    "Route to get user search history"

    @access_control(Config.ROLE_ADMIN)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        """
        Get user search history by user id
        """
        user_id = request.args.get("user_id")
        history_obj = HistoryController(user_id)
        return history_obj.view_user_history()


@blp.route("/history/me")
class UserHistoryMe(MethodView):
    "Route to get logged in user search history"

    @access_control(Config.ROLE_USER)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        """
        Get own search history
        """
        claims = get_jwt()
        user_id = claims.get("sub")
        history_obj = HistoryController(user_id)
        return history_obj.view_user_history()
