from flet_mvc import FletView
import flet as ft
from flet import *
from flet_core import Container



# View
class HomeView(FletView):
    
    
    def __init__(self, controller):
        from mvc.Controller.HomeC import HomeController as HomeC
        self.controller = HomeC
        
    def main(self, page: Page, user_id, username):
        print("user_id:", user_id)
        print("username:", username)

        BG = '#333333'
        FWG = '#97b4ff'
        FG = '#F2F2F2'
        PINK = '#eb06ff'
        WHITE = 'FWG'
        BLACK = '#000000'

        page.title = 'Home Page'
    
        categories_card = Row(
            scroll='auto'
        )

        # Temporary projects, to be changed by user
        categories = ['Project 1', 'Project 2', 'Project 3', 'Project 4', 'Project 5', 'Project 6', 'Project 7', 'Project 8', 'Project 9', 'Project 10']
        for category in categories:
            tasks = ['Task 1', 'Task 2', 'Task 3']  # Placeholder for tasks
            task_controls = []
            for task in tasks:
                task_controls.append(
                    Row(
                        alignment='center',
                        controls=[
                            Checkbox(),  # Placeholder for checkbox, initially unchecked
                            Text(task, color='WHITE', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                        ]
                    )
                )
            categories_card.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=BG, 
                    height=260, 
                    width=400,
                    padding=15,
                    content=Column(
                        controls=[
                            Text(category, color='WHITE', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                            Text('# Tasks', color='WHITE'), # Number of tasks
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
        p = page
        first_page_contents = Container(
            content = Column(
                spacing = 15,
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Container(
                                content=Icon(icons.LOGOUT, color=BLACK),
                                on_click = lambda e: self.back_button_click(p)
                            )
                        ]
                    ),
                    Container(height=20),
                    Text(
                        value = f'Welcome, {username}!',
                        color=BLACK,
                        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM
                    ),
                    Text(
                        value = 'On-Going Projects:',
                        color=BLACK,
                        theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM
                    ),
                    Container(
                        padding=20,
                        content = categories_card
                    ),
                    ElevatedButton("New Project", bgcolor=BG, color="white", on_click=self.create_project_button_click)
                ]
            )
        )

        page_1 = Container()
        page_2 = Row(
            controls=[
                Container(
                    width = 1080,
                    height = 720,
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

        container = Container(
            width=1080,
            height=720,
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
        
    def back_button_click(self, page):
        from mvc.View.LoginV import LoginView as LoginV
        from mvc.Controller.LoginC import LoginController as LoginC
        print("Back Button Clicked")
        page.clean()
        LV = LoginV(LoginC())
        LV.main(page)
        
    
    def create_project_button_click(self, sender):
        print("Create Project Button Clicked")
        # Route to Create Project
        pass
