from time import sleep

from yandextest.YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    sleep(5)
    yandex_main_page.enter_word('Hello')
    elements = yandex_main_page.check_navigation()
    print(elements)