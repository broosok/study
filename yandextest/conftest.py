from selenium import webdriver
import pytest

@pytest.fixture(scope="session")
def browser():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

