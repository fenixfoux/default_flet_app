from utiles.all_variables import list_of_pages
from utiles.settings import AppSettings


def go_home(event):
    event.page.go('/')


def get_all_pages(lang):
    return list_of_pages.get(lang, [])


def get_page_name(lang, key):
    print(f"function 'get_page_name' received: 'lang': '{lang}', 'page_to_go': '{key}'")
    pages = list_of_pages.get(lang, [])
    for page in pages:
        if page['key'] == key:
            print('='*50)
            return page['name']
    return "Page not found"


def go_to_page(event, current_page, page_to_go=None, lang=None) -> None:
    """
        Creates a link and triggers the route change handler from the router.

        This function is typically used to handle page navigation and, optionally, switch languages if provided.

        Args:
            event (ControlEvent): The Flet event triggered by an onClick event.
            current_page (str): The key of the current page where the onClick event was raised.
            page_to_go (str): The key of the page to navigate to.
            lang (str, optional): The language to switch to. This is typically used when switching languages
                                  from the settings page or the app bar. The language is usually saved in a JSON file
                                  and automatically loaded when a page is created, so this parameter is optional only in
                                  these two cases because in that type is created possibility to trigger the route_change
                                  handler (maybe in future i will change that approach, now i don't know hox xD).

        Returns:
            None
    """
    # print(f"function go_to_page starts")
    if page_to_go is None:
        page_to_go = event.control.key
    if lang:
        settings = AppSettings()
        settings.set_property(property_name='language', property_value=lang)
        link = f'from_page/{current_page}/to_page/{page_to_go}/lang/{lang}'
    else:
        link = f'from_page/{current_page}/to_page/{page_to_go}'
    # print(event.control.key)
    # print(f"received: 'current_page': '{current_page}', 'page_to_go': '{page_to_go}'")
    # print(f"created even root is: '{link}'")
    # print(f"created even root is: '{link.split('/')}'")
    event.page.clean()
    event.page.go(link)
    event.page.update()
