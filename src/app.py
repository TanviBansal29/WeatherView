import logging
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from config.config import Config
from config.flask_config import appconfig
from config.jwt_config import jwt_config
from config.register_blueprints import register_blueprints


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%M-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename="logs.log",
)

load_dotenv()
logger = logging.getLogger(__name__)


def create_app():
    """Initialises flask application"""

    app = Flask(__name__)
    logger.info(Config.START_APP)
    appconfig(app)
    jwt = JWTManager(app)
    jwt_config(jwt)
    register_blueprints(app)
    logger.info(Config.END_APP)
    return app


create_app()
