from playwright.sync_api import Page
from elements_practice.base_page import BasePage
from elements_practice.page_factory.button import Button
from elements_practice.page_factory.div import Div

from elements_practice.page_factory.uploader import Uploader

class UploaderPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.uploader = UploaderComponent(page)

class UploaderComponent:
    def __init__(self, page: Page):
        self.page = page

        self.uploader_locator = Uploader(page,locator='//*[@id="file-upload"]', name='Uploader')
        self.submit = Button(page, locator='//*[@id="file-submit"]', name='Submit')
        self.confirmation_text = Div(page, locator='//*[@id="uploaded-files"]', name='Confirmation')

    def upload(self, file_path: str) -> None:
        self.uploader_locator.upload(file_path)
        self.submit.click()
        self.confirmation_text.should_have_text(file_path)