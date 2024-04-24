from math import ceil
from tkinter import CENTER
from turtle import update
from types import CellType
import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page: Page) -> None:
    page.title = 'Project Tracker'
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        

        # Home Page
        page.views.append(
            View(
                route='/', # Home Page / Index Page ; Should work as an App and as a Webb App
                
                controls=[
                        AppBar(title=Text('Home'), bgcolor='blue'),
                        Text(value='Home', size=30),
                        ElevatedButton(text='Button', on_click=lambda _: page.go('/project'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                    
            )
        )

        # Project Page
        if page.route == '/project':
            page.views.append(
            View(
                route='/project', 
                
                controls=[
                        AppBar(title=Text('Project'), bgcolor='blue'),
                        Text(value='Project', size=30),
                        ElevatedButton(text='Back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                    
            )
        )
            

        page.update()
        
    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
if __name__ == '__main__':
    ft.app(target=main)