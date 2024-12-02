import asyncio
import flet as ft

from pages.pages_router import page_route_change_handler


async def main(one_page: ft.Page):
    # check for data bases, and create them if they don't exist
    # check_for_todo_db()

    one_page.window.min_width = 320

    async def async_route_change(e):
        await page_route_change_handler(one_page)

    one_page.on_route_change = async_route_change  # Set the async handler
    await page_route_change_handler(one_page)  # Handle the initial route

    one_page.go(one_page.route)
    one_page.update()


# Wrap the async `main` function
ft.app(target=lambda page: asyncio.run(main(page)))
