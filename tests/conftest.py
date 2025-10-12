import pytest
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser