from flet_mvc import FletController
import flet as ft

from mvc.Model.LoginM import LoginModel
from mvc.View.LoginV import LoginView

# Controller
class LoginController(FletController):
    def __init__(self):
        self.model = LoginModel()
        self.view = LoginView(self)
    
    def main(self):
        self.view.main()
