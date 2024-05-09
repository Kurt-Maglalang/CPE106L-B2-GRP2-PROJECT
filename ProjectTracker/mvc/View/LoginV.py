from flet_mvc import FletView
import flet as ft
from flet import Row, Container, MainAxisAlignment, Text, Column, ElevatedButton, TextField, Page

from mvc.View.RegisterV import RegisterView as RegisterV
from mvc.View.HomeV import HomeView as HomeV

class LoginView(FletView):
    def __init__(self, controller):
        self.controller = controller
        
    def main(self, page: Page):
        page.title = "Login Page"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
 
        username_field = TextField(label="Username", color="white")
        password_field = TextField(label="Password", color="white")
        login_button = ElevatedButton("Log In", bgcolor="#F2F2F2", color="black")
        login_button.on_click = lambda e: self.login_button_click(page, username_field.value, password_field.value)
        register_button = ElevatedButton("Create an Account", bgcolor="#F2F2F2", color="black")
        register_button.on_click = lambda e: self.register_button_click(page)

        container = Container(
            width=1080,
            height=720,
            border_radius=35, 
            bgcolor="white", 
            content = Row (
                alignment=MainAxisAlignment.CENTER,
                controls = [
                    Column (
                        alignment=MainAxisAlignment.CENTER,
                        controls=[            
                            Text("Project Tracker", size=50, color="black"),
                            Container(height=10),
                            Container(
                                padding=10,
                                border_radius=10,
                                bgcolor="#333333",
                                content=Column(
                                    [
                                        Text("Login Account", size=30, color="white"),
                                        username_field,
                                        password_field,
                                        login_button,
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
    
    def login_button_click(self, page, username, password):
        print("Login Button Clicked")
        # Call the authenticate_user method of the controller and take user id
        if self.controller.authenticate_user(username, password):
            user_id = self.controller.get_user_id(username)
            passusername = username #fsr it cant pass 'username' into the method, so had to make another variable-
            print("Success")
            page.clean()
            HomeV(self.controller).main(page, user_id, passusername)          

            
    def register_button_click(self, page):
        print("Register Button Clicked")
        page.clean()
        RegisterV(self.controller).main(page)