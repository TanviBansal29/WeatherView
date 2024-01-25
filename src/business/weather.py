from api_handler.api_client import ApiClient
from config.config import Config


class Weather:
    def __init__(self, city_name=None, lat=None, lon=None):
        self.city_name = city_name
        self.lat = lat
        self.lon = lon

    def get_weather_by_city(self):
        query_data = {Config.CITY_INPUT: self.city_name}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        return data

    def get_weather_by_coordinates(self):
        query_data = {Config.LAT: self.lat, Config.LON: self.lon}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        return data

    def get_forecast(self, days):
        query_data = {Config.CITY: self.city_name, Config.DAYS: days}
        api = ApiClient()
        data = api.forecast_info(query_data)
        return data
