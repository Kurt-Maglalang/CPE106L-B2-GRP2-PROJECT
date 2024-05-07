from flet_mvc import FletController
import flet as ft

from mvc.Model.HomeM import HomeModel
from mvc.View.HomeV import HomeView

# Controller
class HomeController(FletController):
    def __init__(self):
        self.model = HomeModel()
        self.view = HomeView(self)
    
    def main(self):
        self.view.main()
