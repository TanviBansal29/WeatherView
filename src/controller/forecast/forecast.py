from business.weather import Weather
from helpers.custom_exceptions import DataNotFound


class ForecastController:
    'Forecast Controller containing methods to view forecast data'

    def __init__(self, city, days):
        # self.user_id = user_id
        self.city = city
        self.days = days
        self.obj_forecast_business = Weather(city_name=self.city)

    
    def view_weather_forecast(self):
        '''
            Return weather forecast data
        '''
        try:
            data = self.obj_forecast_business.get_forecast(self.days)
            return data
        except DataNotFound as e:
            return {"status" : 404 , "message": str(e)},404