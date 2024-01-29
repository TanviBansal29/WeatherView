import datetime
import os
import logging
import requests
from dotenv import load_dotenv
from config.config import Config

load_dotenv()

logger = logging.getLogger(__name__)

class ApiClient:
    """
        Makes API calls to get weather data and forecast data
    """

    def __init__(self):
        self.url_weather = Config.WEATHER_URL
        self.url_forecast = Config.FORECAST_URL
        self.headers_weather = {
            Config.X_RAPIDAPI_KEY : os.getenv(Config.SECRET_KEY),
            Config.X_RAPIDAPI_HOST : Config.API_HOST,
        }
        self.headers_forecast = {
            Config.X_RAPIDAPI_KEY : os.getenv(Config.SECRET_KEY_FORECAST),
            Config.X_RAPIDAPI_HOST : Config.FORECAST_API_HOST,
        }


    def get_data_by_city(self, query_data):
        """
        Function to get weather data by city name and latitude longitude
        """
        logger.debug(Config.WEATHER_DATA_CITY)
        try:
            response = requests.get(
                self.url_weather,
                headers=self.headers_weather,
                params=query_data,
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            weather_data = []
            self.__parse_weather_response(weather_data, data)
            self.__parse_astro_data(weather_data, data)
            logger.info(Config.CITY_WEATHER_DATA)
            return weather_data
        except requests.exceptions.RequestException as e:
            logger.error(Config.CITY_WEATHER_DATA_ERROR)


    def forecast_info(self, query_data):
        """
        Function to get weather forecast data
        """
        logger.debug(Config.FORECAST_WEATHER_DATA)
        try:
            response = requests.get(
                self.url_forecast,
                headers=self.headers_forecast,
                params=query_data,
                timeout=5
            )
            response.raise_for_status()
            data = response.json().get(Config.TYPE_FORECAST)
            if data:
                forecast_data = self.__parse_forecast_response(data)
                logger.info(Config.WEATHER_FORECAST_SUCCESS)
                return forecast_data
        except requests.exceptions.RequestException as e:
            logger.error(Config.WEATHER_FORECAST_ERROR)


    def __parse_forecast_response(self, data):
        """
        Private function to parse forecast response
        """
        logger.debug(Config.PARSE_FORECAST_RESPONSE)
        forecast_data = []
        for forecast_day in data.get(Config.FORECAST_DAY):
            forecastday_data = []
            forecastday_data.append(forecast_day.get(Config.DATE))
            self.__parse_weather_response(forecastday_data, forecast_day.get(Config.DAY))
            self.__parse_astro_data(forecastday_data, forecast_day.get(Config.ASTRO))
            forecast_data.append(forecastday_data)
        return forecast_data


    def __parse_weather_response(self, weather_data, data):
        """
        Private function to parse weather response
        """
        logger.debug(Config.PARSE_WEATHER_RESPONSE)
        weather_data.append(data.get("maxtemp_c") or data.get("max_temp"))
        weather_data.append(data.get("mintemp_c") or data.get("min_temp"))
        weather_data.append(data.get("maxwind_mph") or data.get("wind_speed"))


    def __parse_astro_data(self, weather_data, data):
        """
        Private function to parse astro data
        """
        logger.debug(Config.PARSE_ASTRO_DATA)
        if data.get(Config.MAXTEMP):
            sunrise_timestamp = data[Config.SUNRISE]
            sunrise_datetime = datetime.datetime.fromtimestamp(sunrise_timestamp)
            data[Config.SUNRISE] = str(sunrise_datetime.strftime(Config.TIME_FORMAT)) + Config.AM
            sunset_timestamp = data[Config.SUNSET]
            sunset_datetime = datetime.datetime.fromtimestamp(sunset_timestamp)
            data[Config.SUNSET] = str(sunset_datetime.strftime(Config.TIME_FORMAT)) + Config.PM 
        weather_data.append(data.get(Config.SUNRISE))
        weather_data.append(data.get(Config.SUNSET))
