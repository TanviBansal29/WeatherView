import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ApiClient:
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
        querystring = query_data
        response = requests.get(
            self.url_weather, headers=self.headers_weather, params=querystring
        )
        if response.status_code in (200, 201):  
            #It's a HTTP status code, it means "OK" (Eg: The server successfully answered the http request).
            data = response.json()
            return data

    def forecast_info(self, query_data):
        querystring = query_data
        response = requests.get(
            self.url_forecast, headers=self.headers_forecast, params=querystring
        )
        data = response.json()
        data = data.get("forecast")

        if data:
            forecast_data = []
            for data in data.get("forecastday"):
                forecastday_data = []
                forecastday_data.append(data.get("date"))
                forecastday_data.append(data.get("day").get("maxtemp_c"))
                forecastday_data.append(data.get("day").get("mintemp_c"))
                forecastday_data.append(data.get("day").get("maxwind_mph"))
                forecastday_data.append(data.get("day").get("daily_chance_of_rain"))
                forecastday_data.append(data.get("astro").get("sunrise"))
                forecastday_data.append(data.get("astro").get("sunset"))
                forecast_data.append(forecastday_data)
        
        return forecast_data