import allure
from playwright.sync_api import expect

from some_more_tests.page_factory.component_base import Component


class DropdownElement(Component):
    @property
    def type_of(self) -> str:
        return "dropdown"

    def select_option(self, option: str, validate_value=False, **kwargs) -> None:
        with allure.step(f'Selecting option "{option}" in dropdown'):
            locator = self.get_locator(**kwargs)
            locator.select_option(value=option)

            if validate_value:
                expect(locator).to_have_value(option)

