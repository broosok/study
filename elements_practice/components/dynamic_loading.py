from playwright.sync_api import Page
from elements_practice.base_page import BasePage
from elements_practice.page_factory.button import Button

from elements_practice.page_factory.dynamic_loading_component import DynamicLoadingComponent

class DynamicLoadingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.dynamic_loading = DynamicLoading(page)

class DynamicLoading:
    def __init__(self, page: Page):
        self.page = page

        self.start_button = Button(page, locator='//button', name='Start button')
        self.element_to_wait = DynamicLoadingComponent(page, locator='//*[@id="finish"]', name='Hello world text')

    def wait_for_text(self, text: str) -> None:
        self.start_button.click()
        self.element_to_wait.wait_for_loading(text)