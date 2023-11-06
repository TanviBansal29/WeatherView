from config.config import Config
from db.helper_functions import fetch_user_data
from db.helper_functions import fetch_user_by_city
from db.helper_functions import view_history
from db.helper_functions import fetch_all_users

def admin_controller():
    print(Config.LOGIN_ADMIN)
    admin_choice = input(Config.ADMIN_PROMPTS)
    while admin_choice != Config.QUIT:
        if admin_choice == Config.FIRST:
            username = input(Config.ENTER_USERNAME)
            fetch_user_data(username)
        elif admin_choice == Config.SECOND:
            fetch_all_users()
            city = input(Config.ENTER_CITYNAME).lower()
            fetch_user_by_city(city)
        elif admin_choice == Config.THIRD:
            fetch_all_users()
            user_id = input(Config.ENTER_USERID)
            view_history(user_id)
        else:
            print(Config.INVALID_INPUT)
        admin_choice = input(Config.ADMIN_PROMPTS)