def appconfig(app):
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "WEATHERVIEW APP"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/weather-view/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["JWT_SECRET_KEY"] = "Tanvi261152921044102586974899032980882739636"
    app.json.sort_keys = False
