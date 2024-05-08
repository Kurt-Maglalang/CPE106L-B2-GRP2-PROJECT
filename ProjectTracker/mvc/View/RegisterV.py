from flet_mvc import FletView

from flet_core import Container

import flet as ft
from flet import Row, Container, MainAxisAlignment, Text, Column, ElevatedButton, TextField, Page

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
        
        # Create container
        container = Container(
            width=1080,
            height=720,
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
        # Call the controller method
        self.controller.create_user(username, password)
