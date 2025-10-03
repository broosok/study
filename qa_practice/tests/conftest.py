from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Firefox()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()