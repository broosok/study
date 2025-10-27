from playwright.sync_api import Page
from elements_practice.base_page import BasePage

from elements_practice.page_factory.dropdown_element import DropdownElement

class DropdownPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.dropdown = DropdownMenu(page)

class DropdownMenu:
    def __init__(self, page: Page):
        self.page = page

        self.select_locator = DropdownElement(page, locator="//select[@id='dropdown']", name="Dropdown")

    def open_dropdown(self, option):
        self.select_locator.select_option(option, validate_value=True)
