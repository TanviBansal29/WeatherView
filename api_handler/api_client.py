import requests
import os
from config.config import Config
from dotenv import load_dotenv
from utils.pretty_print import get_table

load_dotenv()

TABLE_HEADER = f"{'Date':20}{'Max temp':10}{'Min temp':10}{'Avg temp':10}{'Windspeed':10}{'Humidity':10}{'Rain':10}{'Sunrise':10}{'Sunset':10}"

class ApiClient:
    def __init__(self):
        self.url_weather = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
        self.url_forecast = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        self.headers_weather = {
            "X-RapidAPI-Key": os.getenv("SECRET_API_KEY_WEATHER"),
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
        }
        self.headers_forecast = {
            "X-RapidAPI-Key": os.getenv("SECRET_API_KEY_FORECAST"),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

    def get_data_by_city(self, query_data):

        querystring = query_data
        response = requests.get(self.url_weather, headers=self.headers_weather, params=querystring)   
        data = response.json()

        if get_table(data) == None:
            print(Config.NO_DATA)
        else:
            print(get_table(data))
        

    def forecast_info(self, query_data):
        querystring = query_data
        response = requests.get(self.url_forecast, headers=self.headers_forecast, params=querystring)
        data = response.json()
        new_data = data["forecast"]["forecastday"]
        print(TABLE_HEADER)

        for index in new_data:    
            print(f'{str(index["date"]):20}{str(index["day"]["maxtemp_c"]):10}{str(index["day"]["mintemp_c"]):10}{str(index["day"]["avgtemp_c"]):10}{str(index["day"]["maxwind_mph"]):10}{str(index["day"]["avghumidity"]):10}{str(index["day"]["daily_chance_of_rain"]):10}{str(index["astro"]["sunrise"]):10}{str(index["astro"]["sunset"]):10}')
        print("----------------------------------------------------------------------------------------\n")

        