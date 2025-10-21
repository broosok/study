from playwright.sync_api import Page

from some_more_tests.base_page import BasePage

class PlaywrightPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)