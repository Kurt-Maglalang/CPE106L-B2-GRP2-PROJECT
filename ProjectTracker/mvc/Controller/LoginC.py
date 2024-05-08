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
        # Call the authenticate_user method of the model
        if self.model.authenticate_user(username, password):
            print("Authentication successful")
        else:
            print("Authentication failed")
