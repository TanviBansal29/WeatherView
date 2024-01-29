import logging
from api_handler.api_client import ApiClient
from config.config import Config

logger = logging.getLogger(__name__)

class Weather:
    def __init__(self, city_name=None, lat=None, lon=None):
        self.city_name = city_name
        self.lat = lat
        self.lon = lon

    def get_weather_by_city(self):
        logger.debug(Config.GET_WEATHER_CITY, self.city_name)
        query_data = {Config.CITY_INPUT: self.city_name}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        logger.info(Config.GET_WEATHER_SUCCESS, self.city_name)
        return data

    def get_weather_by_coordinates(self):
        logger.debug(Config.GET_WEATHER_COORDINATES, self.lat, self.lon)
        query_data = {Config.LAT: self.lat, Config.LON: self.lon}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        logger.info(Config.GET_WEATHER_COORDINATES_SUCCESS, self.lat, self.lon)
        return data

    def get_forecast(self, days):
        logger.debug(Config.GET_FORECAST, self.city_name, days)
        query_data = {Config.CITY: self.city_name, Config.DAYS: days}
        api = ApiClient()
        data = api.forecast_info(query_data)
        logger.info(Config.GET_FORECAST_SUCCESS, self.city_name, days)
        return data
