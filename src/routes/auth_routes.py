from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import get_jwt, jwt_required
from schemas.schemas import LoginSchema, UserRegisterSchema
from controller.auth.login import LoginController
from controller.auth.register import RegisterController
from controller.auth.logout import LogoutController
from controller.auth.refresh import RefreshController

blp = Blueprint(
    "Authentication", __name__, description="Operations on authentication task"
)


@blp.route("/login")
class Login(MethodView):
    "Route to login an existing user"

    @blp.arguments(LoginSchema)
    def post(self, login_data):
        "Login an existing user"
        login_obj = LoginController(login_data)
        return login_obj.login()


@blp.route("/register")
class Register(MethodView):
    "Route to register a new user"

    @blp.arguments(UserRegisterSchema)
    def post(self, register_data):
        "Register a new user"
        register_obj = RegisterController(register_data)
        return register_obj.register()


@blp.route("/logout")
class Logout(MethodView):
    "Route to logout user"

    @jwt_required()
    def post(self):
        "Logout a logged in user"
        jti = get_jwt().get("jti")
        logout_obj = LogoutController(jti)
        return logout_obj.logout()


@blp.route("/refresh")
class Refresh(MethodView):
    "Route to get a non fresh access token"

    @jwt_required(refresh=True)
    def post(self):
        "Getting a non fresh access token from refresh token"
        claims = get_jwt()
        user_id = claims.get("sub")
        role = claims.get("role")
        refresh_obj = RefreshController(user_id, role)
        return refresh_obj.refresh()
