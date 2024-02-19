from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt
from flask_smorest import Blueprint
from config.config import Config
from config.constants import AUTHORIZATION_HEADER
from helpers import access_control
from controller.weather.weather import WeatherController

blp = Blueprint("Weather", __name__, description="Routes for getting current weather")


@blp.route("/weather/place")
class CurrentWeatherPlace(MethodView):
    "Route to get current weather"

    @access_control(Config.ROLE_USER)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        """
        Get current weather information by place name
        """
        claims = get_jwt()
        user_id = claims.get("sub")
        city = request.args.get("placename")
        weather_obj = WeatherController(user_id, city=city)
        return weather_obj.view_current_weather_by_place()


@blp.route("/weather/coordinates")
class CurrentWeatherCoordinates(MethodView):
    "Route to get current weather"

    @access_control(Config.ROLE_USER)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        """
        Get current weather information by place name
        """
        claims = get_jwt()
        user_id = claims.get("sub")
        lat = request.args.get("lat")
        lon = request.args.get("lon")
        weather_obj = WeatherController(user_id, lat=lat, lon=lon)
        return weather_obj.view_current_weather_by_coordinates()
