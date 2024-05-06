from flet_mvc import FletView

from flet_core import Container

import flet as ft
from flet import Row, Container, MainAxisAlignment, Text, Column, ElevatedButton, TextField, Page


class LoginView(FletView):
    def __init__(self, controller):
        self.controller = controller
        
    def main(self, page: Page):
        page.title = "Login Page"
        
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.horizontal_alignment=ft.MainAxisAlignment.CENTER
        
        container = Container(
            width=1080,
            height=720,
            border_radius=35, 
            bgcolor="blue200",
            
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
                                    bgcolor="blue",
                                    content=Column(
                                        [
                                        Text("Login Account", size=30, color="white"),
                                        TextField(label="Username", color="black"),
                                        TextField(label="Password", color="black"),
                                        ElevatedButton("Log In", bgcolor="blue", color="white"), #on_click = CONTROLLER (self,e)
                                        ElevatedButton("Create an Account", bgcolor="blue", color="white") #on_click = CONTROLLER (self,e)
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
        page.add(container)











    # def __init__(self, controller):
    #     # Define colors
    #     self.controller = controller
    #     self.BG_COLOR = '#FFFFFF'  # Background color
    #     self.TEXT_COLOR = '#333333'  # Text color
    #     self.INPUT_BG_COLOR = '#F2F2F2'  # Input background color
    #     self.BUTTON_BG_COLOR = '#007BFF'  # Button background color
    #     self.BUTTON_TEXT_COLOR = '#FFFFFF'  # Button text color
        
    #     # Initialize the main container
    #     self.container = self.main()

    # def main(self):
    #     # Main container with padding for spacing
    #     login_container = Container(
    #         width=400,
    #         height=300,
    #         bgcolor=self.BG_COLOR,
    #         border_radius=20,
    #         padding=20,
    #         content=Stack(
    #             controls=[
    #                 Text(value="Login", size=24, color=self.TEXT_COLOR),
    #                 TextField(value="Username", bgcolor=self.INPUT_BG_COLOR),
    #                 TextField(value="Password", bgcolor=self.INPUT_BG_COLOR, password=True),
    #                 ft.ElevatedButton(text="Log In", bgcolor=self.BUTTON_BG_COLOR, color=self.BUTTON_TEXT_COLOR)
    #             ]
    #         )
    #     )

    #     return login_container

    # def get_container(self):
    #     return self.container

