import logging
from views.main_menu import MainMenu
from config.config import Config

logging.basicConfig(
    format = Config.LOGGING_FORMAT,
    datefmt = Config.DATE_TIME_FORMAT,
    level = logging.DEBUG,
    filename = Config.LOGS_LOCATION
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(Config.APP_START)
    MainMenu.start_menu()
    logger.info(Config.APP_END)
    