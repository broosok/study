from qa_practice.pages.like_a_button import LikeAButtonPage
import allure

@allure.feature('Like a button')
@allure.story('Existence')
def test_button2_exist(browser):
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.open()
    assert like_a_button_page.button_is_displayed

@allure.feature('Like a button')
@allure.story('Clickability')
def test_button2_clicked(browser):
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.open()
    like_a_button_page.button_click()
    like_a_button_page.check_text()