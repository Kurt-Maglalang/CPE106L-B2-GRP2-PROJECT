import flet as ft
from flet_mvc import RouteHandler

# Home
from mvc.Model.HomeM import HomeModel
from mvc.View.HomeV import HomeView
from mvc.Controller.HomeC import HomeController



def main(page: ft.page):
    # Set up MVC
    routes = RouteHandler(page)
    
    # Initializations
    HomeM = HomeModel()
    HomeV = HomeView()
    HomeC = HomeController()

    # Properties

    # Run
    page.go(page.route)
    
ft.app(target=main)