from business.authentication import Authentication


class LogoutController:
    '''
        Logout Controller class containing logout method
    '''

    def __init__(self, token_id):
        self.token_id = token_id
        self.obj_auth_business = Authentication()

    def logout(self):
        self.obj_auth_business.logout(self.token_id)
        response = {
            "status_code": 200,
            "message": "SUCCESSFULLY LOGGED OUT"
        }
        return response

