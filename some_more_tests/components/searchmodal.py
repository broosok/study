from playwright.sync_api import Page

from some_more_tests.page_factory.input import Input
from some_more_tests.page_factory.title import Title
from some_more_tests.page_factory.list_item import ListItem

class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.empty_result_title = Title(page, locator='p.DocSearch-Help', name='Empty results')

        self.search_input = Input(page, locator='#docsearch-input', name='Search docs')

        self.search_result = ListItem(
            page, locator='#docsearch-hits{result_number}-item-{result_number}', name='Result item'
        )

    def modal_is_opened(self) -> None:
        self.search_input.should_be_visible()
        self.empty_result_title.should_be_visible()

    def find_result(self, keyword: str, result_number: int) -> None:
        self.search_input.fill(keyword, validate_value=True)
        self.search_result.click(result_number=result_number)
        
