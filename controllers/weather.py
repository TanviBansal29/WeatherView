from api_handler.api_client import ApiClient
from config.config import Config

class Weather:
    def get_weather_by_city(city_name):
        query_data = {Config.CITY_INPUT:city_name}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        return data

    def get_weather_by_cordinates(lat, lon):
        query_data = {Config.LAT : lat ,Config.LON : lon}
        api = ApiClient()
        data = api.get_data_by_city(query_data)
        return data

    def get_forecast(city_name):
        days =  int(input(Config.ENTER_DAYS))
        query_data = {Config.CITY : city_name ,Config.DAYS : days}
        api = ApiClient()
        data = api.forecast_info(query_data)
        return data
       
