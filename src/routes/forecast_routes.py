from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from config.config import Config
from config.constants import AUTHORIZATION_HEADER
from helpers import access_control
from controller.forecast.forecast import ForecastController

blp = Blueprint("Forecast", __name__, description="Routes for getting weather forecast")


@blp.route("/forecast")
class ForecastData(MethodView):
    "Route to get weather forecast"

    @access_control(Config.ROLE_USER)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        """
        Get weather forecast by city name and number of days
        """
        city = request.args.get("city")
        days = request.args.get("days")
        forecast_obj = ForecastController(city, days)
        return forecast_obj.view_weather_forecast()
