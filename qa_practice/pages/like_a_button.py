from selenium.webdriver.common.by import By
from qa_practice.pages.base_page import BasePage
from qa_practice.pages.simple_button import result_selector
from yandextest.conftest import browser
import allure

URL = 'https://www.qa-practice.com/elements/button/like_a_button'
button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')

class LikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open Like a button URL'):
            self.browser.get(URL)

    @property
    def button(self):
        return self.find(button_selector)

    @property
    def button_is_displayed(self):
        with allure.step('Check that button is displayed'):
            return self.button.is_displayed()

    def button_click(self):
        with allure.step('Click the button'):
            self.button.click()

    @property
    def result(self):
        return self.find(result_selector)

    @property
    def text(self):
        with allure.step('Get result text'):
            return self.result.text

    def check_text(self):
        with allure.step('Check result'):
            assert 'Submitte' == self.text