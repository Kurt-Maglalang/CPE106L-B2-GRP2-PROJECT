from flet_mvc import FletController
from mvc.Model.RegisterM import RegisterModel
from mvc.View.RegisterV import RegisterView

class RegisterController(FletController):
    def __init__(self):
        self.model = RegisterModel()
        self.view = RegisterView(self)
    
    def main(self):
        self.view.main()
    
    def create_user(self, username, password):
        # Call the create_user method of the model
        try:
            self.model.create_user(username, password)
            print("User created successfully")
        except Exception as e:
            print("Error creating user:", e)
