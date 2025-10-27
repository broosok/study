import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from some_more_tests.pages.playwrighthomepage import PlaywrightPage
from some_more_tests.pages.playwrightlanguagepage import PlayWrightLanguagesPage

@pytest.fixture(scope="function")
def chromium_page():
    with sync_playwright() as p:
        chromium = p.chromium.launch(headless=False)
        yield chromium.new_page()

@pytest.fixture(scope="function")
def playwright_homepage(chromium_page: Page) -> PlaywrightPage:
    return PlaywrightPage(chromium_page)

@pytest.fixture(scope="function")
def playwright_languages_page(chromium_page: Page) -> PlayWrightLanguagesPage:
    return PlayWrightLanguagesPage(chromium_page)
