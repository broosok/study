from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.ya.ru/'

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      f'Could not locate element {locator}')

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      f'Could not locate elements {locator}')

    def go_to_site(self):
        return self.driver.get(self.base_url)