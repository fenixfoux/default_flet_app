import flet as ft

from pages.home_page import HomePage
from utiles.static_functions import get_page_name


class DummyPage1(HomePage):
    def __init__(self):
        super().__init__()
        self.is_home = False
        self.previous_page_key = ''
        self.current_page_key = ''
        self.content_page = ft.Column()
        self.app_bar = self.create_appbar()
        self.additional_appbar_actions = []

    def create_additional_appbar_actions(self) -> list:
        """create and return a list of button widgets for using them next to appbar's actions buttons"""
        self.additional_appbar_actions.extend([
            # ft.TextButton(icon=ft.icons.AUTO_FIX_HIGH, on_click=lambda e: self.test_something(e)),
            ft.TextButton('wof'),
            ft.TextButton('bong')
        ])
        return self.additional_appbar_actions

    def create_content_page(self) -> ft.Column:
        self.content_page.controls = [
            ft.Text(f"This is {self.page_name} page"),
        ]
        # self.content_page.alignment = ft.MainAxisAlignment.END
        # self.content_page.height = 400
        # self.content_page.width = 500

        return self.content_page
