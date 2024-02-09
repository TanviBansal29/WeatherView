import logging
from api_handler.api_client import ApiClient
from config.config import Config
from helpers import DataNotFound

logger = logging.getLogger(__name__)


class Weather:
    def __init__(self, city_name=None, lat=None, lon=None):
        self.city_name = city_name
        self.lat = lat
        self.lon = lon

    def get_weather_by_city(self):
        """Function to get weather data for city"""

        logger.info("Getting weather by city")

        query_data = {Config.CITY_INPUT: self.city_name}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        if not data:
            raise DataNotFound(Config.NO_DATA)
        response = {
            "Min_temp (°C)": data[0],
            "Max_temp (°C)": data[1],
            "windspeed (m/hr)": data[2],
            "sunrise": data[3],
            "sunset": data[4],
        }
        return response

    def get_weather_by_coordinates(self):
        """Function to get weather data by coordinates"""

        logger.info("Getting weather by coordinates")

        query_data = {Config.LAT: self.lat, Config.LON: self.lon}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        if not data:
            raise DataNotFound(Config.NO_DATA)
        response = {
            "Min_temp (°C)": data[0],
            "Max_temp (°C)": data[1],
            "Windspeed (m/hr)": data[2],
            "Sunrise": data[3],
            "Sunset": data[4],
        }

        return response

    def get_forecast(self, days):
        """Function to get weather forecast data"""

        logger.info("Getting weather forecast")

        query_data = {Config.CITY: self.city_name, Config.DAYS: days}
        api = ApiClient()
        data = api.forecast_info(query_data)
        if not data:
            raise DataNotFound(Config.NO_DATA)
        response = {}
        forecast_data = []
        for item in data:
            response = {
                "Date": item[0],
                "Max_temp (°C)": item[1],
                "Min_temp (°C)": item[2],
                "Windspeed (m/hr)": item[3],
                "Sunrise": item[4],
                "Sunset": item[5],
            }
            forecast_data.append(response)
        return forecast_data
