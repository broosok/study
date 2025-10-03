import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture()
def browser():
    firefox_browser = webdriver.Firefox()
    firefox_browser.implicitly_wait(10)
    return firefox_browser

def test_button2_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.LINK_TEXT, 'Click').is_displayed()

def test_button2_clicked(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    browser.find_element(By.LINK_TEXT, 'Click').click()
    assert 'Submitted' == browser.find_element(By.ID, 'result-text').text