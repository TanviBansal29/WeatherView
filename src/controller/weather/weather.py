from business.weather import Weather
from helpers import ParseResponse, handle_errors


class WeatherController:
    "Weather Controller containing methods to view current weather information"

    def __init__(self, user_id, city=None, lat=None, lon=None):
        self.user_id = user_id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.obj_forecast_business = Weather(
            self.user_id, city_name=self.city, lat=self.lat, lon=self.lon
        )
        self.response = ParseResponse()

    @handle_errors
    def view_current_weather_by_place(self):
        """
        Return current weather information by place name
        """

        data = self.obj_forecast_business.get_weather_by_city()
        return self.response.success_response(data)

    @handle_errors
    def view_current_weather_by_coordinates(self):
        """
        Return current weather information by place name
        """

        data = self.obj_forecast_business.get_weather_by_coordinates()
        return self.response.success_response(data)
