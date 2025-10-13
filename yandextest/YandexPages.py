from selenium.webdriver import Keys

from yandextest.baseapp import BasePage
from selenium.webdriver.common.by import By

class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.XPATH, '/html/body/div[1]/div[1]/nav/div[1]')

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.send_keys(Keys.RETURN)
        return search_field


    def check_navigation(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=20)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu



