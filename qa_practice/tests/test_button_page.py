from qa_practice.pages.simple_button import SimpleButtonPage
import allure


@allure.feature('Simple button')
@allure.story('Existence')
def test_button1_exist(browser):
    with allure.step('Open Simple Button URL'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Check the button existence'):
        assert simple_page.button_is_displayed()


@allure.feature('Simple button')
@allure.story('Clickability')
def test_button1_clicked(browser):
    with allure.step('Open Simple Button URL'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Click the button'):
        simple_page.click_button()
    with allure.step('Check result'):
        assert 'Submitted' == simple_page.result_text

