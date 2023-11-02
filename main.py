from main_menu import MainMenu
from config.config import Config
from db.helper_functions import create_user_table

if __name__ == '__main__':
    Config.load_print_statements()
    Config.load_queries()
    Config.load_prompts()
    create_user_table()
    MainMenu.start_menu()

    