from pwinput import pwinput
from config.config import Config
from db.helper_functions import verify_username
from db.helper_functions import create_user
from db.helper_functions import verify_user
from db.helper_functions import fetch_role

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
                print()
                user_choice = input(Config.USER_PROMPTS)
                while user_choice != 'q':
                    if user_choice == '1':
                        #all weather info
                        pass
                    elif user_choice == '2':
                        #forecasting
                        pass
                    else:
                        print(Config.INVALID_INPUT)
                    user_choice = input(Config.USER_PROMPTS)