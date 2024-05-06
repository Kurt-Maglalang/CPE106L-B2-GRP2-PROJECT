import flet as ft
from flet import *

class LogIn(UserControl):
    def __init__(self):
        super(LogIn, self).__init__()
        self.username = TextField(label="Username")
        self.username = TextField(label="Password")
        
    def main(self):
        return Container(
            bgcolor="yellow200",
            padding=10,
            content=Column([
                Text("Login Account", size=30),
                self.username,
                self.password,
                ElevatedButton("Log In", bgcolor="blue", color="white", on_click=self.loginbtn),
                ElevatedButton("Register", bgcolor="blue", color="white", on_click=self.registerbtn)

                    ]
                )
            )
    def loginbtn(self,e):
        pass
        # This might be handled in the controller instead
    
    def registerbtn(self, e):
        pass
        # This might be handled in the controller instead