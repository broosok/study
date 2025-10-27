import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from elements_practice.components.dropdown_menu import DropdownPage

@pytest.fixture(scope="function")
def chromium_page():
    with sync_playwright() as p:
        chromium = p.chromium.launch(headless=False)
        yield chromium.new_page()

@pytest.fixture(scope="function")
def dropdown_page(chromium_page: Page) -> DropdownPage:
    return DropdownPage(chromium_page)