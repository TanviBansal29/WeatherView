import logging
from dotenv import load_dotenv
from flask import Flask, request
from flask_jwt_extended import JWTManager
from config.config import Config
from config.flask_config import appconfig
from config.jwt_config import jwt_config
import shortuuid
from config.register_blueprints import register_blueprints
from db.database import db


load_dotenv()
logging.getLogger().handlers = []
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%M-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename="logs.log",
)

logger = logging.getLogger(__name__)


def create_admin():
    db.add_item(
        Config.QUERY_TO_CREATE_ADMIN,
        ("AD1234", "admin", "adminadmin", "noida", 201305, "admin"),
    )


def create_app():
    """Initialises flask application"""
    app = Flask(__name__)
    logger.info(Config.START_APP)
    appconfig(app)
    jwt = JWTManager(app)
    jwt_config(jwt)
    register_blueprints(app)

    create_admin()

    # @app.before_request
    # def pre_request_handler():
    #     """Adds request id to logs"""
    #     request_id = shortuuid.ShortUUID().random(length=6)
    #     request.request_id = request_id

    logger.info(Config.END_APP)
    return app


flask_app = create_app()
