import logging
from main_menu import MainMenu
from config.config import Config
from db.helper_functions import create_user_table
from db.helper_functions import create_history_table

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG, filename='utils/logs.log')
logger = logging.getLogger("main")

@Config.loader
def main():
    logger.info('App started')
    create_user_table()
    create_history_table()
    MainMenu.start_menu()
    logger.info('App ended')

main()

# if __name__ == '__main__':
#     logger.info('App started')
#     Config.load_print_statements()
#     Config.load_queries()
#     Config.load_prompts()
#     create_user_table()
#     create_history_table()
#     MainMenu.start_menu()
#     logger.info('App ended')

    