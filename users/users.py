from datetime import datetime
from api_handler.api_client import ApiClient
from config.config import Config
from db.helper_functions import insert_history
from db.helper_functions import view_history

def user_controller(user_id):
    print(Config.LOGIN_USER)
    user_input = input(Config.USER_VIEW_PROMPTS)
    while user_input != Config.QUIT:
        if user_input == Config.FIRST:
            user_choice = input(Config.USER_PROMPTS)
            while user_choice != Config.QUIT:
                if user_choice == Config.FIRST:
                    city_name = input(Config.ENTER_CITYNAME)
                    tm = datetime.now()
                    dt_string = tm.strftime(Config.FORMAT_DATE_TIME)
                    searched_by = Config.CITY_NAME
                    searched_for = Config.CURRENT_WEATHER
                    insert_history(user_id, searched_for, searched_by, dt_string, city_name)
                    query_data = {Config.CITY_INPUT:city_name}
                    ap = ApiClient()
                    ap.get_data_by_city(query_data)
                    break
                elif user_choice == Config.SECOND:
                    lat = float(input(Config.LATITUDE))
                    lon = input(Config.LONGITUDE)
                    tm = datetime.now()
                    dt_string = tm.strftime(Config.FORMAT_DATE_TIME)
                    searched_by = Config.LAT_LON
                    searched_for = Config.CURRENT_WEATHER
                    insert_history(user_id, searched_for, searched_by, dt_string, "-")
                    query_data = {Config.LAT : lat, Config.LON : lon}
                    ap = ApiClient()
                    ap.get_data_by_city(query_data)
                    break
                else:
                    print(Config.INVALID_INPUT)
                user_choice = input(Config.USER_PROMPTS)
        elif user_input == Config.SECOND:
            city_name = input(Config.ENTER_CITYNAME)
            tm = datetime.now()
            dt_string = tm.strftime(Config.FORMAT_DATE_TIME)
            searched_by = Config.CITY_NAME
            searched_for = Config.FORECAST
            insert_history(user_id, searched_for, searched_by, dt_string, city_name)
            days =  int(input(Config.ENTER_DAYS))
            query_data = {Config.CITY : city_name , Config.DAYS : days}
            ap = ApiClient()
            ap.forecast_info(query_data)
        elif user_input == Config.THIRD:
            view_history(user_id)
            pass
        else:
            print(Config.INVALID_INPUT)
        user_input = input(Config.USER_VIEW_PROMPTS)

