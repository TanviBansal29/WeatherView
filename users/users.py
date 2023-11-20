import os
from tabulate import tabulate
from config.config import Config
from controllers.history import History
from controllers.weather import Weather
from utils.pretty_print import get_table


def user_controller(user_id):
    print(Config.LOGIN_USER)
    user_input = input(Config.USER_VIEW_PROMPTS)
    while user_input != Config.QUIT:
        if user_input == Config.FIRST:
            user_choice = input(Config.USER_PROMPTS)
            while user_choice != Config.QUIT:
                if user_choice == Config.FIRST:
                    city_name = input(Config.ENTER_CITYNAME)
                    data = Weather.get_weather_by_city(city_name)
                    if data:
                        print(get_table(data))
                    History.insert_history(user_id,city_name)
                    break

                elif user_choice == Config.SECOND:
                    lat = float(input(Config.LATITUDE))
                    lon = input(Config.LONGITUDE)
                    Weather.get_weather_by_cordinates(lat, lon)
                    History.insert_history(user_id,"-")
                    break
                else:
                    print(Config.INVALID_INPUT)
                user_choice = input(Config.USER_PROMPTS)

        elif user_input == Config.SECOND:
            city_name = input(Config.ENTER_CITYNAME)
            Weather.get_forecast(city_name)
            History.insert_history(user_id, city_name)

        elif user_input == Config.THIRD:
            data = History.view_history(user_id)
            if data:
                HEADERS  = ["date time", "searched_for", "searched_by", "city_name"]
                print(tabulate(data,headers=HEADERS,tablefmt=Config.TABLE_FORMAT))
            else:
                print(Config.NO_DATA)

        else:
            print(Config.INVALID_INPUT)

        user_input = input(Config.USER_VIEW_PROMPTS)

