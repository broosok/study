import pytest

from some_more_tests.pages.playwrighthomepage import PlaywrightPage
from some_more_tests.pages.playwrightlanguagepage import PlayWrightLanguagesPage


class TestSearch:
    @pytest.mark.parametrize('keyword', ['python'])
    def test_search(self, keyword: str, playwright_homepage: PlaywrightPage,
                    playwright_languages_page: PlayWrightLanguagesPage
                    ) -> None:
        playwright_homepage.visit('https://playwright.dev')
        playwright_homepage.navigation.open_search()
        playwright_homepage.navigation.search_modal.find_result(keyword, result_number=0)
        playwright_languages_page.language_present(language=keyword)