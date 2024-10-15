import flet as ft
from utiles.all_variables import languages, HOME_PAGE_KEY
from utiles.settings import AppSettings
from utiles.static_functions import go_home, get_page_name, get_all_pages, go_to_page


class HomePage:
    def __init__(self):
        self.is_home = True
        self.previous_page_key = ''
        self.current_page_key = HOME_PAGE_KEY
        self.current_settings = AppSettings()
        self.selected_language = AppSettings().get_property(property_name='language')
        self.all_pages = get_all_pages(self.selected_language)
        # self.page_name = get_page_name(self.selected_language, self.current_page_key)
        self.page_name = ''
        self.app_bar = self.create_appbar()
        self.content_page = ft.Column()

    def create_appbar(self, current_page_name='', is_home=False) -> ft.AppBar:
        home_button_visible = not is_home
        language_widgets = ft.PopupMenuButton(icon=ft.icons.LANGUAGE)

        for lang in languages:
            current_lang_icon = ft.icons.RADIO_BUTTON_UNCHECKED
            if lang == self.selected_language:
                current_lang_icon = ft.icons.RADIO_BUTTON_CHECKED_OUTLINED

            language_widgets.items.append(
                ft.PopupMenuItem(
                    on_click=lambda e, l=lang: self.switch_language(l, e),  # Pass the language to switch
                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Icon(name=current_lang_icon),
                            ft.Text(lang)
                        ]
                    )
                )
            )
            if languages.index(lang) < len(languages) - 1:
                language_widgets.items.append(ft.PopupMenuItem())  # divider

        self.app_bar = ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=40,
            title=ft.Text(current_page_name, no_wrap=True),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.TextButton(icon=ft.icons.AUTO_FIX_HIGH, on_click=lambda e: self.test_something(e)),
                ft.IconButton(ft.icons.HOME, on_click=go_home, visible=home_button_visible),
                ft.IconButton(ft.icons.FILTER_3),
                language_widgets,
            ],
        )
        return self.app_bar

    def test_something(self, e):
        """function for test different things"""
        print(f"test button was pressed on home page :D")

    def switch_language(self, new_language, e):
        if new_language != self.selected_language:
            # Update the language setting
            self.selected_language = new_language
            self.current_settings.set_property(property_name='language', property_value=self.selected_language)
            # Recreate the whole page (app bar and content) based on the new language
            self.page_name = get_page_name(self.selected_language, self.current_page_key)
            self.all_pages = get_all_pages(self.selected_language)

            # Recreate app bar and content
            e.page.views.clear()  # Clear views to refresh the page
            updated_appbar = self.create_appbar(self.page_name, is_home=self.is_home)
            e.page.views.append(
                ft.View(
                    "/",
                    [ft.SafeArea(content=self.create_content_page())],
                    appbar= updated_appbar
                )
            )
            e.page.update()  # Trigger full update to reflect the language change

    def update_ui(self, e):
        self.app_bar.update()
        e.page.update()

    def create_content_page(self):
        # Clear any existing controls before rebuilding the content
        self.content_page.controls.clear()

        # Add new content based on the current pages
        for page in self.all_pages:
            if page['key'] != self.current_page_key:
                self.content_page.controls.append(
                    ft.TextButton(
                        text=f"go to page: {page['name']}, 'page_key'= {page['key']}",
                        key=page['key'],
                        on_click=lambda ev: go_to_page(ev, current_page=self.current_page_key)
                    )
                )
        self.content_page.controls.append(ft.Text(self.page_name))

        # Return the content column so it can be displayed
        return self.content_page
