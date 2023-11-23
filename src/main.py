import logging
from main_menu import MainMenu
from db.database import db


logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG, filename='src/utils/logs.log')
logger = logging.getLogger("main")


logger.info('App started')
MainMenu.start_menu()
logger.info('App ended')

