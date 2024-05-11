import flet as ft

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
    print("Started")

    # Call Database Setup method
    databaseSetup.create_database()
    
    # Login
    LoginM = LoginModel()
    LoginC = LoginController()    
    LoginM.controller = LoginController()
    LoginV = LoginView(LoginC)
    
    # Register
    RegisterM = RegisterModel()
    RegisterM.controller = RegisterController()
    RegisterC = RegisterController()
    RegisterV = RegisterView(RegisterC)

    # Home
    HomeM = HomeModel()
    HomeC = HomeController()
    HomeM.controller = HomeController()
    HomeV = HomeView(HomeC)
    
    # Page Properties
    page.title = "Project Tracker"
    page.window_width = 1100
    page.window_height = 1000

    # Run
    LoginV.main(page)
    
ft.app(target=main, assets_dir="Images")