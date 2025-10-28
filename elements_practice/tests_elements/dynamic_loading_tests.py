import pytest

from elements_practice.components.dynamic_loading import DynamicLoadingPage


class TestDynamicLoadingPage:

    @pytest.mark.parametrize('text', ['Hello World!'])
    def test_dynamic_loading(self, dynamic_page: DynamicLoadingPage, text: str) -> None:
        dynamic_page.visit("https://the-internet.herokuapp.com/dynamic_loading/2")
        dynamic_page.dynamic_loading.wait_for_text(text)