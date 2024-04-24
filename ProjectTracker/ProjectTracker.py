from mvc.controller import Controller
from mvc.view import Home
from mvc.model import Model

import flet as ft

def Main(page):
    # Set up MVC
    model = Model()
    controller = Controller() # May have arguments
    model.controller = controller 
    view = Home() # May have arguments
    

    # Run
    
ft.app(target=main)