from qa_practice.pages.simple_button import SimpleButtonPage
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture()
def browser():
    firefox_browser = webdriver.Firefox()
    firefox_browser.implicitly_wait(10)
    return firefox_browser

def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert 'Submitted' == simple_page.result_text

