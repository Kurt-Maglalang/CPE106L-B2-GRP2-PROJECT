# This is a placeholder .py file just to make sure that VS2022 can commit to this repository

import flet as ft
from flet import (
    Container,
    Icon,
    Page,
    colors,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    icons,
    margin
)
from flet_core.colors import LIGHT_BLUE_ACCENT


class TrelloApp:
    def __init__(self, page: Page):
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="login"),    
            PopupMenuItem(), # Divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width = 100,
            title=Text("Trolli", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appBar_items
                        ),
                    margin = margin.only(left=50, right=25)    
                    )
                ],
            )
        self.page.appbar = self.appbar
        self.page.update()

if __name__ == "__main__":

    def main(page: Page):
        page.title = "Trello Clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = TrelloApp(page)
        page.add(app)
        page.update()

    ft.app(target=main, view=ft.WEB_BROWSER)
    
