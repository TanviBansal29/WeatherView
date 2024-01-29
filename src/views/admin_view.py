import os
from config.config import Config
from handler.history import History
from handler.user import User
from helpers.table_helper import TableHelper


class AdminHelper:
    def admin_controller(self):
        os.system('cls')
        print(Config.LOGIN_ADMIN)
        admin_choice = input(Config.ADMIN_PROMPTS)
        while admin_choice != Config.QUIT:
            if admin_choice == Config.FIRST:
                self.__get_user_data_helper()

            elif admin_choice == Config.SECOND:
                self.__get_user_by_city_helper()

            elif admin_choice == Config.THIRD:
                self.__get_user_history_helper()

            else:
                print(Config.INVALID_INPUT)
            admin_choice = input(Config.ADMIN_PROMPTS)

    def __get_user_data_helper(self):
        data = self.__get_user_data()
        if data:
            TableHelper.print_table(data, type=Config.TYPE_USERNAME)
        else:
            print(Config.NO_DATA)

    @staticmethod
    def __get_user_data():
        username = input(Config.ENTER_USERNAME)
        user = User(username)
        data = user.fetch_user_data()
        return data

    def __get_user_by_city_helper(self):
        user = User()
        user.fetch_all_users()
        data = self.__get_user_by_city()
        if data:
            TableHelper.print_table(data, type=Config.TYPE_CITY)
        else:
            print(Config.NO_DATA)

    def __get_user_history_helper(self):
        user = User()
        user.fetch_all_users()
        data = self.__get_user_history()
        if data:
            TableHelper.print_table(data, type=Config.TYPE_HISTORY)
        else:
            print(Config.NO_DATA)

    @staticmethod
    def __get_user_by_city():
        city = input(Config.ENTER_CITYNAME).lower()
        user = User(city=city)
        data = user.fetch_user_by_city()
        return data

    @staticmethod
    def __get_user_history():
        user_id = input(Config.ENTER_USERID)
        history_obj = History(user_id)
        data = history_obj.view_history()
        return data
    