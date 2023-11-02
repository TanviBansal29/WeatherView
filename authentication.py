from pwinput import pwinput
from config.config import Config
from db.helper_functions import verify_username
from db.helper_functions import create_user
from db.helper_functions import verify_user
from db.helper_functions import fetch_role
from api_handler.api_calling import ApiCalling

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
            role = fetch_role(username, password)
            if role == 'admin':
                print(Config.LOGIN_ADMIN)
                admin_choice = input(Config.ADMIN_PROMPTS)
                while admin_choice != 'q':
                    if admin_choice == '1':
                        #view user data
                        pass
                    elif admin_choice == '2':
                        #view by place 
                        pass
                    else:
                        print(Config.INVALID_INPUT)
                    admin_choice = input(Config.ADMIN_PROMPTS)        
                
            else:
                user_input = input(Config.USER_VIEW_PROMPTS)
                while user_input != 'q':
                    if user_input == '1':
                        user_choice = input(Config.USER_PROMPTS)
                        while user_choice != 'q':
                            if user_choice == '1':
                                city_name = input("Enter city name: ")
                                query_data = {"city":city_name}
                                ap = ApiCalling()
                                ap.get_data_by_city(query_data)
                                break
                            elif user_choice == '2':
                                lat = int(input("Enter latitutde: "))
                                lon = input("Enter longitude: ")
                                query_data = {"lat" : lat, "lon" : lon}
                                ap = ApiCalling()
                                ap.get_data_by_city(query_data)
                                break
                            else:
                                print(Config.INVALID_INPUT)
                            user_choice = input(Config.USER_PROMPTS)
                    elif user_input == '2':
                        pass
                    else:
                        print("INAVLID INPUT. PLEASE TRY AGAIN!!")
                    user_input = input(Config.USER_VIEW_PROMPTS)