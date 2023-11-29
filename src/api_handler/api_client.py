import datetime
import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class ApiClient:
    """
        Makes api call to get weather data and forecast data
    """

    def __init__(self):
        self.url_weather = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
        self.url_forecast = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        self.headers_weather = {
            "X-RapidAPI-Key": os.getenv("SECRET_API_KEY_WEATHER"),
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com",
        }
        self.headers_forecast = {
            "X-RapidAPI-Key": os.getenv("SECRET_API_KEY_FORECAST"),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        }

    def get_data_by_city(self, query_data):
        """
            Function to get weather data by cityname and latitude longitude
        """
        logger.debug('Fetching weather data')
        querystring = query_data
        response = requests.get(
            self.url_weather, headers=self.headers_weather, params=querystring, timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            weather_data = []
            self.__parse_weather_response(weather_data, data)
            self.__parse_astro_data(weather_data, data)
            return weather_data
        

    def forecast_info(self, query_data):
        """
            Function to get weather forecast data
        """
        logger.debug('Fetching weather forecast data')
        querystring = query_data
        response = requests.get(
            self.url_forecast, headers=self.headers_forecast, params=querystring, timeout=5
        )
        data = response.json()
        data = data.get("forecast")

        if data:
            forecast_data = self.__parse_forecast_response(data)
            return forecast_data

    def __parse_forecast_response(self, data):
        """
        Private function to get forecast response
        """
        logger.debug('Running parse_forecast_response')
        forecast_data = []
        for data in data.get("forecastday"):
            forecastday_data = []
            forecastday_data.append(data.get("date"))
            self.__parse_weather_response(forecastday_data, data.get("day"))
            self.__parse_astro_data(forecastday_data, data.get("astro"))
            forecast_data.append(forecastday_data)
        return forecast_data

    def __parse_weather_response(self, weather_data, data):
        """
            Private function to get weather response
        """
        logger.debug('Running parse_weather_response')
        weather_data.append(data.get("maxtemp_c") or data.get("max_temp"))
        weather_data.append(data.get("mintemp_c") or data.get("min_temp"))
        weather_data.append(data.get("maxwind_mph") or data.get("wind_speed"))

    def __parse_astro_data(self, weather_data, data):
        """
            Private function to get astro data
        """
        logger.debug('Running parse_astro_data')
        if data.get("max_temp"):
            timestamp = data['sunrise']
            datetime_obj = datetime.datetime.fromtimestamp(timestamp)
            data["sunrise"] = str(datetime_obj.strftime('%H:%M:%S')) + ' A.M.'
            timestamp = data['sunset']
            datetime_obj = datetime.datetime.fromtimestamp(timestamp)
            data["sunset"] = str(datetime_obj.strftime('%H:%M:%S')) + ' P.M.'
        weather_data.append(data.get("sunrise"))
        weather_data.append(data.get("sunset"))
