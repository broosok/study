from qa_practice.pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')
URL = 'https://www.qa-practice.com/elements/button/simple'

class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        
    def open(self):
        self.browser.get(URL)

    def button(self):
        return self.find(button_selector)

    def click_button(self):
        self.button().click()

    def button_is_displayed(self):
        return self.button().is_displayed()

    def result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.result().text