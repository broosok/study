import allure
from playwright.sync_api import expect

from some_more_tests.page_factory.component_base import Component


class Input(Component):

    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, validate_value=False, **kwargs) -> None:
        with allure.step(f"Filling {self.type_of} with value {value}"):
            locator = self.get_locator(**kwargs)
            locator.fill(value)

            if validate_value:
                self.should_have_text(value, **kwargs)

    def should_have_text(self, value: str, **kwargs) -> None:
        with allure.step(f"Checking {self.type_of} have text {value}"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)

