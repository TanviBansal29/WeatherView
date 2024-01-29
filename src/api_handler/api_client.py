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
        logger.debug("Fetching weather data for city.")
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
            logger.info("Weather data fetched successfully for city")
            return weather_data
        except requests.exceptions.RequestException as e:
            logger.error("Error fetching weather data for city")


    def forecast_info(self, query_data):
        """
        Function to get weather forecast data
        """
        logger.debug("Fetching weather forecast data")
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
                logger.info("Weather forecast data fetched successfully")
                return forecast_data
        except requests.exceptions.RequestException as e:
            logger.error("Error fetching weather forecast data: %s", str(e))


    def __parse_forecast_response(self, data):
        """
        Private function to parse forecast response
        """
        logger.debug("Parsing forecast response")
        forecast_data = []
        for forecast_day in data.get("forecastday"):
            forecastday_data = []
            forecastday_data.append(forecast_day.get("date"))
            self.__parse_weather_response(forecastday_data, forecast_day.get("day"))
            self.__parse_astro_data(forecastday_data, forecast_day.get("astro"))
            forecast_data.append(forecastday_data)
        return forecast_data


    def __parse_weather_response(self, weather_data, data):
        """
        Private function to parse weather response
        """
        logger.debug("Parsing weather response")
        weather_data.append(data.get("maxtemp_c") or data.get("max_temp"))
        weather_data.append(data.get("mintemp_c") or data.get("min_temp"))
        weather_data.append(data.get("maxwind_mph") or data.get("wind_speed"))


    def __parse_astro_data(self, weather_data, data):
        """
        Private function to parse astro data
        """
        logger.debug("Parsing astro data")
        if data.get(Config.MAXTEMP):
            sunrise_timestamp = data[Config.SUNRISE]
            sunrise_datetime = datetime.datetime.fromtimestamp(sunrise_timestamp)
            data[Config.SUNRISE] = str(sunrise_datetime.strftime('%H:%M:%S')) + ' A.M.'
            sunset_timestamp = data[Config.SUNSET]
            sunset_datetime = datetime.datetime.fromtimestamp(sunset_timestamp)
            data[Config.SUNSET] = str(sunset_datetime.strftime('%H:%M:%S')) + ' P.M.'
        weather_data.append(data.get(Config.SUNRISE))
        weather_data.append(data.get(Config.SUNSET))
