# login
# logout
# register
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.schemas import LoginSchema, UserRegisterSchema
from controller.auth.login import LoginController
from controller.auth.register import RegisterController

blp = Blueprint("Authentication", __name__, description="Operations on authentication task")

@blp.route("/login")
class Login(MethodView):
    'Route to login an existing user'

    @blp.arguments(LoginSchema)
    def post(self, login_data):
        'Login an existing user'
        login_obj = LoginController(login_data)
        return login_obj.login()

@blp.route("/register")
class Register(MethodView):
    'Route to register a new user'

    @blp.arguments(UserRegisterSchema)
    def post(self, register_data):
        'Register a new user'
        register_obj = RegisterController(register_data)
        return register_obj.register()

@blp.route("/logout")
class Logout(MethodView):
    def post(self):
        pass