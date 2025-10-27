import pytest

from elements_practice.components.dropdown_menu import DropdownPage

class TestDropdownPage:

    @pytest.mark.parametrize('option', ['1'])
    def test_dropdown_page(self, dropdown_page: DropdownPage, option: str) -> None:
        dropdown_page.visit("https://the-internet.herokuapp.com/dropdown")
        dropdown_page.dropdown.open_dropdown(option=option)
