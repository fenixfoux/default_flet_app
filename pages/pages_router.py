import flet as ft

from pages.dummy_page_1 import DummyPage1
from pages.home_page import HomePage
from utiles.settings import AppSettings
from utiles.static_functions import get_page_name


def page_route_change_handler(page):
    page.update()
    print(f"event open new page initiated")
    home_page = HomePage()
    home_page.selected_language = AppSettings().get_property(property_name='language')
    home_page.page_name = get_page_name(home_page.selected_language, home_page.current_page_key)
    home_page_content = home_page.create_content_page()
    home_page_appbar = home_page.create_appbar(home_page.page_name, is_home=True)
    pages = {
        '/': ft.View(
            "/",
            [ft.SafeArea(content=home_page_content)],
            appbar=home_page_appbar
        ),
    }

    # link example: from_page/previous_page_name/to_page/next_page_name
    if page.route.startswith('from_page'):
        # print(f"received path: {page.route}")
        # print(f"split received path: {page.route.split('/')}")
        split_received_path = page.route.split('/')
        page_to_go_key = split_received_path[3]
        previous_page_key = split_received_path[1]

        if page_to_go_key == 'dummy_1':
            dummy_1_page = DummyPage1()
            dummy_1_page.previous_page_key = previous_page_key
            dummy_1_page.current_page_key = page_to_go_key
            # dummy_1_page.selected_language = dummy_1_page.selected_language
            # dummy_1_page.page_name = get_page_name(dummy_1_page.selected_language, dummy_1_page.current_page_key)
            def_appbar = dummy_1_page.create_appbar(
                    current_page_name=dummy_1_page.page_name,
                    is_home=dummy_1_page.is_home
                )
            def_appbar.actions = dummy_1_page.create_additional_appbar_actions() + def_appbar.actions
            dummy_1_page_content = dummy_1_page.create_content_page()
            pages[page.route] = ft.View(
                route=page.route,
                controls=[ft.SafeArea(content=dummy_1_page_content)],
                appbar=def_appbar
            )

    page.views.clear()
    page.views.append(pages.get(page.route, pages['/']))
    page.update()


