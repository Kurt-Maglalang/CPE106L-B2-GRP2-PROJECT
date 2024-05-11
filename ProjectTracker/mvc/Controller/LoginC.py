from flet_mvc import FletController
from mvc.Model.LoginM import LoginModel
from mvc.View.LoginV import LoginView

class LoginController(FletController):
    def __init__(self):
        self.model = LoginModel()
        self.view = LoginView(self)
    
    def main(self):
        self.view.main()
    
    def authenticate_user(self, username, password):
        if self.model.authenticate_user(username, password):
            print("Authentication successful")
            return True
        else:
            print("Authentication failed")
            return False
        
    def get_user_id(self, user_id):
        return self.model.get_user_id(user_id)