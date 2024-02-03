from business.authentication import Authentication


class RefreshController:
    """
    Refresh Controller class containing refresh token generation method
    """

    def __init__(self, user_id, role):
        self.user_id = user_id
        self.role = role
        self.obj_auth_business = Authentication()

    def refresh(self):
        new_access_token = self.obj_auth_business.refresh(self.user_id, self.role)
        return {"access_token": new_access_token}
