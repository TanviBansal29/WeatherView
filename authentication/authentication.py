from pwinput import pwinput
from config.config import Config
from db.helper_functions import verify_user
from db.helper_functions import fetch_role_and_id
from db.helper_functions import insert_history
from db.helper_functions import fetch_user_data
from db.helper_functions import fetch_user_by_city
from db.helper_functions import view_history
from db.helper_functions import fetch_all_users
from api_handler.api_client import ApiClient
from datetime import datetime

class Authentication:
        @staticmethod
        def login():
            while True:
                username = input(Config.ENTER_USERNAME)
                password = pwinput(Config.ENTER_PASSWORD)
                if not verify_user(username, password):
                    continue
                else: 
                    break
            role, user_id = fetch_role_and_id(username, password)
            if role == 'admin':
                print(Config.LOGIN_ADMIN)
                admin_choice = input(Config.ADMIN_PROMPTS)
                while admin_choice != 'q':
                    if admin_choice == '1':
                        username = input(Config.ENTER_USERNAME)
                        fetch_user_data(username)
                    elif admin_choice == '2':
                        fetch_all_users()
                        city = input(Config.ENTER_CITYNAME)
                        fetch_user_by_city(city)
                    elif admin_choice == '3':
                        fetch_all_users()
                        user_id = input(Config.ENTER_USERID)
                        view_history(user_id)
                    else:
                        print(Config.INVALID_INPUT)
                    admin_choice = input(Config.ADMIN_PROMPTS)        
                
            else:
                print(Config.LOGIN_USER)
                user_input = input(Config.USER_VIEW_PROMPTS)
                while user_input != 'q':
                    if user_input == '1':
                        user_choice = input(Config.USER_PROMPTS)
                        while user_choice != 'q':
                            if user_choice == '1':
                                city_name = input(Config.ENTER_CITYNAME)
                                tm = datetime.now()
                                dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
                                insert_history(user_id,dt_string, city_name)
                                query_data = {"city":city_name}
                                ap = ApiClient()
                                ap.get_data_by_city(query_data)
                                break
                            elif user_choice == '2':
                                lat = float(input(Config.LATITUDE))
                                lon = input(Config.LONGITUDE)
                                query_data = {"lat" : lat, "lon" : lon}
                                ap = ApiClient()
                                ap.get_data_by_city(query_data)
                                break
                            else:
                                print(Config.INVALID_INPUT)
                            user_choice = input(Config.USER_PROMPTS)
                    elif user_input == '2':
                        city_name = input(Config.ENTER_CITYNAME)
                        tm = datetime.now()
                        dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
                        insert_history(user_id, dt_string, city_name)
                        days =  int(input(Config.ENTER_DAYS))
                        query_data = {"q" : city_name , "days" : days}
                        ap = ApiClient()
                        ap.forecast_info(query_data)
                    elif user_input == '3':
                        view_history(user_id)
                        pass
                    else:
                        print(Config.INVALID_INPUT)
                    user_input = input(Config.USER_VIEW_PROMPTS)