import logging
from views.main_menu import MainMenu
# from config.config import Config
import hashlib
# from db.database import db

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%M-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename='src/logs.log'
)

# def create_admin():
#     query = 'INSERT INTO users (user_id, username, password, city, zipcode, role) VALUES (%s, %s, %s, %s, %s, %s)'
#     password = 'adminadmin'
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     data = ('Ayd28Pc', 'admin', hashed_password, 'Noida', '201305', 'admin')
#     db.add_item(query, data)


logger = logging.getLogger("main")

if __name__ == "__main__":
    logger.info('App started')
    # create_admin()
    MainMenu.start_menu()
    logger.info('App ended')







