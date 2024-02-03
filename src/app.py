import logging
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from config.flask_config import appconfig
from config.jwt_config import jwt_config
from routes.auth_routes import blp as AuthRoutes
from routes.forecast_routes import blp as ForecastRoutes
from routes.user_routes import blp as UserRoutes
from routes.weather_routes import blp as WeatherRoutes
from routes.history_routes import blp as HistoryRoutes

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%M-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename="logs.log",
)
load_dotenv()
logger = logging.getLogger("main")


def create_app():
    """Initialises flask application"""

    app = Flask(__name__)
    logger.info("App started")
    appconfig(app)
    api = Api(app)
    jwt = JWTManager(app)
    jwt_config(jwt)

    api.register_blueprint(AuthRoutes, url_prefix="/weather-view")
    api.register_blueprint(ForecastRoutes, url_prefix="/weather-view")
    api.register_blueprint(UserRoutes, url_prefix="/weather-view")
    api.register_blueprint(WeatherRoutes, url_prefix="/weather-view")
    api.register_blueprint(HistoryRoutes, url_prefix="/weather-view")

    logger.info("App ended")
    return app


create_app()
