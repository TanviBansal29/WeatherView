import logging
from flask import Flask, jsonify 
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from views.main_menu import MainMenu
# from config.config import Config
import hashlib
# from db.database import db
from routes.auth_routes import blp as AuthRoutes
from routes.forecast_routes import blp as ForecastRoutes
from routes.user_routes import blp as UserRoutes
from routes.weather_routes import blp as WeatherRoutes
from routes.history_routes import blp as HistoryRoutes

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%M-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename='logs.log'
)

# def create_admin():
#     query = 'INSERT INTO users (user_id, username, password, city, zipcode, role) VALUES (%s, %s, %s, %s, %s, %s)'
#     password = 'adminadmin'
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     data = ('Ayd28Pc', 'admin', hashed_password, 'Noida', '201305', 'admin')
#     db.add_item(query, data)


logger = logging.getLogger("main")


def create_app():

    app = Flask(__name__)
    app.json.sort_keys = False
    logger.info('App started')

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "WEATHERVIEW APP"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/weather-view/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "Tanvi261152921044102586974899032980882739636"
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    api.register_blueprint(AuthRoutes,url_prefix="/weather-view")
    api.register_blueprint(ForecastRoutes,url_prefix="/weather-view")
    api.register_blueprint(UserRoutes,url_prefix="/weather-view")
    api.register_blueprint(WeatherRoutes,url_prefix="/weather-view")
    api.register_blueprint(HistoryRoutes,url_prefix="/weather-view")

    # print(app.url_map)
    logger.info('App ended')
    return app