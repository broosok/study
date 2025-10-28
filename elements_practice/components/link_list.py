from playwright.sync_api import Page
from elements_practice.base_page import BasePage

from elements_practice.page_factory.link import Link

class LinkPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.linklist = LinkList(page)

class LinkList:
    def __init__(self, page: Page):
        self.page = page

        self.link_locator = Link(page, locator='//a[@href="download/{file_name}"]', name="Link")

    def download(self, file_name: str) -> None:
        print(f"Downloading file: {file_name}, type: {type(file_name)}")
        self.link_locator.click(file_name=file_name)