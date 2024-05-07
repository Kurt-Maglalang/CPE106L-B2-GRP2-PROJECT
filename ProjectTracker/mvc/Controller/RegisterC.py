from flet_mvc import FletController
import flet as ft

from mvc.Model.RegisterM import RegisterModel
from mvc.View.RegisterV import RegisterView

# Controller
class RegisterController(FletController):
    def __init__(self):
        self.model = RegisterModel()
        self.view = RegisterView(self)
    
    def main(self):
        self.view.main()
