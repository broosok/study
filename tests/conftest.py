import pytest
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    firefox_browser = webdriver.Firefox(options=options)
    firefox_browser.implicitly_wait(10)
    return firefox_browser