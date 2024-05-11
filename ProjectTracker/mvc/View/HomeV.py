# Importing necessary modules and classes
from flet_mvc import FletView
import flet as ft
from flet import *
from flet_core import Container

# View class for the home page
class HomeView(FletView):
    
    def __init__(self, controller):
        from mvc.Controller.HomeC import HomeController as HomeC
        self.controller = HomeC # it wouldnt work so i just directly did it

    def main(self, page: Page, user_id, username):
        from mvc.Controller.HomeC import HomeController as HomeC
        # Styling constants
        BG = '#333333'
        FWG = '#97b4ff'
        FG = '#F2F2F2'
        PINK = '#eb06ff'
        WHITE = 'FWG'
        BLACK = '#000000'
        
        # Set page title
        page.title = 'Home Page'

        # Retrieve user's projects and tasks
        categories_card = Row(
            scroll='auto'
        )
        categories = self.controller.fetch_user_projects(user_id)
        for category in categories:
            project_name = str(category).strip("(),'")
            try:
                project_id = HomeC.get_project_id_by_name(project_name)
                tasks = self.controller.fetch_project_tasks(project_id)
                task_controls = []
                for task_id, task in enumerate(tasks):
                    # Create task controls (checkbox and task name)
                    task_name = str(task).strip("(),'")
                    task_controls.append(
                        Row(
                            alignment='center',
                            controls=[
                                Checkbox(value=self.controller.fetch_task_state(task_id), on_change=lambda e: self.toggle_task_status(task_id)),
                                Text(task_name, color='WHITE', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                            ]
                        )
                    )

            except Exception as e:
                print("Failed to load tasks:",e)

            # Add project details and associated tasks to the categories card
            categories_card.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=BG, 
                    height=260, 
                    width=400,
                    padding=15,
                    content=Column(
                        controls=[
                            Text(project_name, color='WHITE', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                            Container(
                                width=160,
                                height=5,
                                bgcolor='white12',
                                border_radius=20,
                                padding=50
                            ),
                            *task_controls  # Unpack task controls
                        ]
                    )
                )
            )

        # Define page contents
        first_page_contents = Container(
            content = Column(
                spacing = 15,
                controls=[
                    # Back button
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Container(
                                content=Icon(icons.LOGOUT, color=BLACK),
                                on_click = lambda e: self.back_button_click(page)
                            )
                        ]
                    ),
                    Container(height=20),
                    # Welcome message
                    Text(
                        value = f'Welcome, {username}!',
                        color=BLACK,
                        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM
                    ),
                    # Section header
                    Text(
                        value = 'Projects:',
                        color=BLACK,
                        theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM
                    ),
                    # Projects and tasks section
                    Container(
                        padding=20,
                        content = categories_card
                    ),
                    # Create project section
                    self.create_project_section(page, user_id, username)
                ]
            )
        )

        # Define page layout
        page_1 = Container()
        page_2 = Row(
            controls=[
                Container(
                    width = 1080,
                    height = 900,
                    bgcolor = FG,
                    border_radius=35,
                    padding=20,
                    content = Column(
                        controls=[
                            first_page_contents
                        ]
                    )
                )
            ]
        )

        # Main container for page
        container = Container(
            width=1080,
            height=900,
            bgcolor=BG,
            border_radius=35, 
            content=Stack(
                controls=[
                    page_1,
                    page_2
                ]
            ) 
        )
        page.add(container)
        
    # Method to handle back button click
    def back_button_click(self, page):
        print("Back Button Clicked")
        # Navigate back to login page
        from mvc.View.LoginV import LoginView as LoginV
        from mvc.Controller.LoginC import LoginController as LoginC
        page.clean()
        LV = LoginV(LoginC())
        LV.main(page)

    # Method to create new project section
    def create_project_section(self, page, user_id, username):
        BG = '#333333'
        project_name_field = TextField(label="Project Name", color="white")
        task_field = TextField(label="Enter Task", color="white")
        add_task_button = ElevatedButton("Add Task", bgcolor="#F2F2F2", color="black", on_click=lambda e: self.add_task_button_click(project_name_field.value, task_field.value)) # project_id, project_name, task_name
        create_project_button = ElevatedButton("Create", bgcolor="#F2F2F2", color="black", on_click=lambda e: self.create_project_button_click(user_id, project_name_field.value)) # self, user_id, project_name

        return Container(
            padding=20,
            content=Column(
                controls=[
                    Text("Create New Project", color="white", size=20),
                    project_name_field,
                    task_field,
                    add_task_button,
                    create_project_button
                ],
                spacing=10
            ),
            border_radius=10,
            bgcolor=BG,
            width=600  # Adjusted width to fit within window
        )

    # Method to handle create project button click
    def create_project_button_click(self, user_id, project_name):
        print('Create Project Button Clicked')
        if project_name:
            if self.controller.create_project(user_id, project_name):
                print("Project created successfully.")
            else:
                print("Failed to create project.")
        else:
            print("No Project Name.")

    # Method to handle add task button click
    def add_task_button_click(project_id, project_name, task_name):
        print("Add Task Button Clicked")
        
        from mvc.Controller.HomeC import HomeController as HomeC
        
        project_id = HomeC.get_project_id_by_name(project_name)

        if project_id:
            if HomeC.create_task(project_id, task_name):
                print("Task created successfully.")
            else:
                print("Task failed successfully.")
        else:
            print("No Project Name.")
                
    # Method to toggle task status
    def toggle_task_status(self, task_id):
        if self.controller.toggle_task_status(task_id):
            print("Task status toggled successfully.")
            # Refresh the page or update tasks dynamically
        else:
            print("Failed to toggle task status.")
