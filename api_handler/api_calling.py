import requests
import os
from dotenv import load_dotenv

load_dotenv()
# city_name = "Noida"
class ApiCalling:
    def __init__(self):
        self.url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
        self.headers = {
            "X-RapidAPI-Key": os.getenv("SECRET_API_KEY"),
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
        }

    def get_data_by_city(self, query_data):

        querystring = query_data
        response = requests.get(self.url, headers=self.headers, params=querystring)
        print(response.json())


obj1 = ApiCalling()
obj1.get_data_by_city({"city": "Varanasi"})        