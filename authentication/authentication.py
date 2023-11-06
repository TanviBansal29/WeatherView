import hashlib
from pwinput import pwinput
from config.config import Config
from db.helper_functions import verify_user
from db.helper_functions import fetch_role_and_id
from users.admin import admin_controller
from users.users import user_controller


class Authentication:
        @staticmethod
        def login():
            while True:
                username = input(Config.ENTER_USERNAME)
                password = pwinput(Config.ENTER_PASSWORD)
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if not verify_user(username, hashed_password):
                    continue
                else: 
                    break
            role, user_id = fetch_role_and_id(username, hashed_password)
            if role == Config.ADMIN:
                admin_controller()
            else: # role == 'user'
                user_controller(user_id)