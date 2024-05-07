from flet_mvc import FletView
import flet as ft
from flet import *
from flet import Page # I have no clue why I imported Page here when I imported all lmao
from flet_core import Container

# View
class HomeView(FletView):
    
    def __init__(self, controller):
        self.controller = controller
        
    def main(self, page: Page):
    # Colors, change as needed
    # We can probably use a theme or something    
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
                            Text('# Tasks', color='WHITE'),
                            Container(
                                width=160,
                                height=5,
                                bgcolor='white12',
                                border_radius=20,
                                padding=padding.only(right=50)
                            )
                        ]
                    )
                )
            )

        first_page_contents = Container(
            content = Column(
                spacing = 15,
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Container(
                                content=Icon(icons.ARROW_BACK_IOS, color=BLACK)
                            )
                        ]
                    ),
                    Container(height=20),
                    Text(
                        value = 'Welcome!',
                        color=BLACK,
                        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM
                    ),
                    Text(
                        value = 'On-Going Projects:',
                        color=BLACK,
                        theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM
                    ),
                    Container(
                        padding=padding.only(top=10,bottom=20,),
                        content = categories_card
                    )
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
                    padding=padding.only( top=50, left=20, right = 20, bottom=5),
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