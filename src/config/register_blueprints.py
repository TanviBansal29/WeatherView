from flask_smorest import Api
from routes.auth_routes import blp as AuthRoutes
from routes.forecast_routes import blp as ForecastRoutes
from routes.user_routes import blp as UserRoutes
from routes.weather_routes import blp as WeatherRoutes
from routes.history_routes import blp as HistoryRoutes


def register_blueprints(app):
    """Function to register blueprints"""

    api = Api(app)

    api.register_blueprint(AuthRoutes, url_prefix="/weather-view")
    api.register_blueprint(ForecastRoutes, url_prefix="/weather-view")
    api.register_blueprint(UserRoutes, url_prefix="/weather-view")
    api.register_blueprint(WeatherRoutes, url_prefix="/weather-view")
    api.register_blueprint(HistoryRoutes, url_prefix="/weather-view")
