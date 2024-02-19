from business.weather import Weather
from helpers import handle_errors, ParseResponse


class ForecastController:
    "Forecast Controller containing methods to view forecast data"

    def __init__(self, user_id, city, days):
        self.user_id = user_id
        self.city = city
        self.days = days
        self.obj_forecast_business = Weather(user_id, city_name=self.city)
        self.response = ParseResponse()

    @handle_errors
    def view_weather_forecast(self):
        """
        Return weather forecast data
        """

        response = self.obj_forecast_business.get_forecast(self.days)
        return self.response.success_response(response)
