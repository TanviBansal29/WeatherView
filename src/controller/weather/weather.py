from business.weather import Weather
from helpers import DataNotFound


class WeatherController:
    "Weather Controller containing methods to view current weather information"

    def __init__(self, city=None, lat=None, lon=None):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.obj_forecast_business = Weather(
            city_name=self.city, lat=self.lat, lon=self.lon
        )

    def view_current_weather_by_place(self):
        """
        Return current weather information by place name
        """
        try:
            data = self.obj_forecast_business.get_weather_by_city()
            return data
        except DataNotFound as e:
            return {"status": 404, "message": str(e)}, 404

    def view_current_weather_by_coordinates(self):
        """
        Return current weather information by place name
        """
        try:
            data = self.obj_forecast_business.get_weather_by_coordinates()
            return data
        except DataNotFound as e:
            return {"status": 404, "message": str(e)}, 404
