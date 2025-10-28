import pytest
from playwright.sync_api import Page, sync_playwright

from elements_practice.components.dropdown_menu import DropdownPage
from elements_practice.components.file_uploader import UploaderPage
from elements_practice.components.link_list import LinkPage


@pytest.fixture(scope="function")
def chromium_page():
    with sync_playwright() as p:
        chromium = p.chromium.launch(headless=False)
        yield chromium.new_page()

@pytest.fixture(scope="function")
def dropdown_page(chromium_page: Page) -> DropdownPage:
    return DropdownPage(chromium_page)

@pytest.fixture(scope="function")
def linklist_page(chromium_page: Page) -> LinkPage:
    return LinkPage(chromium_page)

@pytest.fixture(scope="function")
def uploader_page(chromium_page: Page) -> UploaderPage:
    return UploaderPage(chromium_page)