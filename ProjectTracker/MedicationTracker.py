import flet as ft

from .mvvm import PlaceholderViewModel  # Use dot (.) for current directory
from mvvm import PlaceholderView

def main(page: ft.Page):
    vm = PlaceholderViewModel()  # Create view model instance
    view = PlaceholderView()  # Create view instance

    page.add(view)  # Add view to the page

ft.app(target=main)
