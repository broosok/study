import pytest

from elements_practice.components.add_remove_component import AddRemovePage

class TestAddRemovePage:

    @pytest.mark.parametrize('click_count', [10])
    def test_add_remove_page(self, add_remove_page: AddRemovePage, click_count: int) -> None:
        add_remove_page.visit('https://the-internet.herokuapp.com/add_remove_elements/')
        add_remove_page.add_remove.add_element(click_count=click_count)