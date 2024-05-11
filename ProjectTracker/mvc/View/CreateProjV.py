from flet_mvc import FletView
import flet as ft
from flet import Row, Container, MainAxisAlignment, Text, Column, ElevatedButton, TextField, Page, Icon

class CreaterProjView(FletView):
    def __init__(self, controller):
        self.controller = controller
        
    def main(self, page: Page):
        page.title = "Create Project"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
 
        project_name_field = TextField(label="Project Name", color="white")
        task_field = TextField(label="Enter Task", color="white")
        add_task_button = ElevatedButton("Add Task", bgcolor="#F2F2F2", color="black")
        add_task_button.on_click = lambda e: self.add_task_button_click(task_field.value)
        confirm_button = ElevatedButton("Confirm Project", bgcolor="#F2F2F2", color="black")
        confirm_button.on_click = lambda e: self.confirm_button_click(project_name_field.value)
        back_button = Container(content=Icon(ft.icons.ARROW_BACK_IOS, color="black"),on_click = lambda e: self.back_button_click(p))
        p = page

        container = Container(
            width=1080,
            height=720,
            border_radius=35, 
            bgcolor="white", 
            content = Row (
                alignment=MainAxisAlignment.CENTER,
                controls = [
                    back_button,
                    Container (
                            padding = 10,
                            border_radius=10,
                            height = 400,
                            bgcolor="#333333",
                            content= Column (
                                alignment=MainAxisAlignment.CENTER,
                                controls=[            
                                Text("Create Project", size=30, color="white"),
                                project_name_field,
                                Text("Tasks:", size=20, color="white "),
                                task_field,
                                add_task_button,
                                confirm_button
                                ]
                            )
                    )
                ]
            )
        )
        page.add(container)
    
    def add_task_button_click(self, task):
        print("Add Task Button Clicked")
        # Call the add_task method of the controller
        # self.controller.add_task(task)
        pass
       
    def confirm_button_click(self, project_name):
        print("Confirm Button Clicked")
        # Call the confirm_project method of the controller
        # self.controller.confirm_project(project_name)
        pass

    def back_button_click(self, page):
        from mvc.View.HomeV import HomeView as HomeV
        from mvc.Controller.HomeC import HomeController as HomeC
        print("Back Button Clicked")
        page.clean()
        HV = HomeV(HomeC())
        HV.main(page)
        

