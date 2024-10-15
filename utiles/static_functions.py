from utiles.all_variables import list_of_pages


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


def go_to_page(event, current_page, page_to_go=None):
    if page_to_go is None:
        page_to_go = event.control.key
    # print(event.control.key)
    # print(f"received: 'current_page': '{current_page}', 'page_to_go': '{page_to_go}'")
    link = f'from_page/{current_page}/to_page/{page_to_go}'
    # print(f"created even root is: '{link}'")
    # print(f"created even root is: '{link.split('/')}'")
    event.page.clean()
    event.page.go(link)
    event.page.update()
