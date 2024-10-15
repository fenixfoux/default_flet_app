import flet as ft

from pages.pages_router import page_route_change_handler


def main(one_page: ft.Page):
    # todo: check for data bases, and create them if doesn't exist
    # check_for_todo_db()

    # one_page.platform = ft.PagePlatform.IOS
    # one_page.update()

    one_page.window.min_width = 320
    one_page.on_route_change = lambda _: page_route_change_handler(one_page)
    one_page.go(one_page.route)

    one_page.update()


ft.app(target=main)


