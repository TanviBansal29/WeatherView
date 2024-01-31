from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from helpers.rbac import access_control
from controller.forecast.forecast import ForecastController

blp = Blueprint("Forecast" ,__name__, description="Routes for getting weather forecast")

@blp.route("/forecast")
class ForecastData(MethodView):
    'Route to get weather forecast'

    @access_control("user")
    def get(self):
        '''
            Get weather forecast by city name and number of days
        '''
        # user_id = request.args.get("user_id")
        city = request.args.get("city")
        days = request.args.get("days")
        forecast_obj = ForecastController(city, days)
        return forecast_obj.view_weather_forecast()