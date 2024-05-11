from flet_mvc import FletView

from flet_core import Container

import flet as ft
from flet import Row, Container, MainAxisAlignment, Text, Column, ElevatedButton, TextField, Page, Icon
from flet import *

class RegisterView(FletView):
    def __init__(self, controller):
        self.controller = controller
    
    def main(self, page: Page):
        page.title = "Registration Page"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
        username_field = TextField(label="Username", color="white")
        password_field = TextField(label="Password", color="white")
        register_button = ElevatedButton("Register", bgcolor="#F2F2F2", color="black")
        register_button.on_click = lambda e: self.handle_register(username_field.value, password_field.value)

        back_button = Icon(ft.icons.ARROW_BACK_IOS, color="#000000")
        back_button.on_click = lambda e: self.back_button_click
        
        p = page

        # Create container
        container = Container(
            width=1080,
            height=900,
            border_radius=35,
            bgcolor="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            # Title
                            Text("Project Tracker", size=50, color="black"),
                            Container(
                                content=Icon(icons.ARROW_BACK_IOS, color="black"),
                                on_click = lambda e: self.back_button_click(p)
                            ),
                            Container(height=10),
                            Container(
                                padding=10,
                                border_radius=10,
                                bgcolor="#333333",
                                content=Column(
                                    [
                                        Text("Create an Account", size=30, color="white"),
                                        username_field, 
                                        password_field, 
                                        register_button 
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        
        page.add(container)
        
    def handle_register(self, username, password):
        from mvc.Controller.RegisterC import RegisterController as RegisterC
        print("Registration Clicked")
        
        if username != "" and password != "":
            # Create an instance of RegisterController
            register_controller = RegisterC()
            # Call the controller method on the instance
            register_controller.create_user(username, password)
        else:
            print("No Input")


    def back_button_click(self, page):
        from mvc.View.LoginV import LoginView as LoginV
        from mvc.Controller.LoginC import LoginController as LoginC
        print("Back Button Clicked")
        page.clean()
        LV = LoginV(LoginC())
        LV.main(page)