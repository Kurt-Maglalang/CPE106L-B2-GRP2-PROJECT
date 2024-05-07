from flet_mvc import FletView

from flet_core import Container

import flet as ft
from flet import Row, Container, MainAxisAlignment, Text, Column, ElevatedButton, TextField, Page


class RegisterView(FletView):
    def __init__(self, controller):
        self.controller = controller
        
    def main(self, page: Page):
        page.title = "Registration Page"
        
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.horizontal_alignment=ft.MainAxisAlignment.CENTER
        
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

                                        # Text Fields for User Input
                                        TextField(label="Username", color="white"),
                                        TextField(label="Password", color="white"),

                                        # Buttons for LogIn/Registration, Needs Event Handlers
                                        ElevatedButton("Register", bgcolor="#F2F2F2", color="black"), #on_click = CONTROLLER (self,e)
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
        )
    
        page.add(container)