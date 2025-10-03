from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    firefox_browser = webdriver.Firefox()
    firefox_browser.implicitly_wait(10)
    return firefox_browser

