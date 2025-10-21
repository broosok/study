from playwright.sync_api import Page

from some_more_tests.page_factory.input import Input
from some_more_tests.page_factory.title import Title
from some_more_tests.page_factory.list_item import ListItem

class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.empty_result_title = Title(page, locator='p.DocSearch-Help', name='Empty results')
