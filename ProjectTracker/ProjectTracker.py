import flet as ft
from flet import app
from flet_mvc import RouteHandler

# Database Imports
from Database.Database_SetUp import databaseSetup

# MVC Imports
from mvc.Model.LoginM import LoginModel
from mvc.Model.RegisterM import RegisterModel
from mvc.Model.HomeM import HomeModel

from mvc.View.LoginV import LoginView
from mvc.View.RegisterV import RegisterView
from mvc.View.HomeV import HomeView

from mvc.Controller.LoginC import LoginController
from mvc.Controller.RegisterC import RegisterController
from mvc.Controller.HomeC import HomeController

def main(page: ft.page):
    routes = RouteHandler(page)

    # Call Database Setup method
    databaseSetup.create_database()
    
    # Login
    LoginM = LoginModel()
    LoginC = LoginController()    
    LoginM.controller = LoginController()
    LoginV = LoginView(LoginC)
    routes.register_route("/", LoginView.main)
    
    # Register
    RegisterM = RegisterModel()
    RegisterC = RegisterController()
    RegisterM.controller = RegisterController()
    RegisterV = RegisterView(RegisterC)
    routes.register_route("/Register", RegisterView.main)

    # Home
    HomeM = HomeModel()
    HomeC = HomeController()
    HomeM.controller = HomeController()
    HomeV = HomeView(HomeC)
    routes.register_route("/Home", HomeView.main)
    
    # Page Properties
    page.title = "Project Tracker"
    page.window_width = 1080
    page.window_height = 780
    page.on_route_change = routes.route_change

    # Run
    # page.go(page.route)
    HomeV.main(page)
    
ft.app(target=main, assets_dir="Images")