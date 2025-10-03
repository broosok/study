import re
from playwright.sync_api import Page, expect
import pytest



def test_has_title(page: Page):

    page.goto('https://playwright.dev/')

    expect(page).to_have_title(re.compile('Playwright'))

def test_get_start_link(page: Page):
    page.goto('https://playwright.dev/')

    page.get_by_role('link', name='Get started').click()

    expect(page.get_by_role('heading', name='Installation')).to_be_visible()

@pytest.fixture(scope='function', autouse=True)
def before_each_after_each(page: Page):
    print('before the test runs')

    page.goto('https://playwright.dev/')
    yield

    print('after the test runs')

def test_main_navigation(page: Page):
    expect(page).to_have_url('https://playwright.dev/')