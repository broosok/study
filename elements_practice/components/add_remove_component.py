from playwright.sync_api import Page, expect
from elements_practice.base_page import BasePage

from elements_practice.page_factory.button import Button

class AddRemovePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_remove = AddRemoveElement(page)

class AddRemoveElement:
    def __init__(self, page: Page):
        self.page = page

        self.add_element_button = Button(page, locator="//button[text()='Add Element']", name='Add Element')
        self.element = Button(page, locator="//button[text()='Delete']", name='Element')

    def add_element(self, click_count: int):
        self.add_element_button.click_multiple_times(click_count)
        self.element.check_value(count=click_count)