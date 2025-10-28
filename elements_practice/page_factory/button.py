import allure
from playwright.sync_api import expect

from some_more_tests.page_factory.component_base import Component


class Button(Component):

    @property
    def type_of(self) -> str:
        return "button"

    def hover(self, **kwargs) -> None:
        with allure.step(f"Hovering to {self.type_of} with name {self.name}"):
            locator = self.get_locator(**kwargs)
            locator.hover()

    def double_click(self, **kwargs) -> None:
        with allure.step(f"Double clicking to {self.type_of} with name {self.name}"):
            locator = self.get_locator(**kwargs)
            locator.dblclick()

    def click_multiple_times(self, click_count: int, **kwargs) -> None:
        with allure.step(f"Clicking multiple times with name {self.name}"):
            locator = self.get_locator(**kwargs)
            for i in range(click_count):
                locator.click()


    def check_value(self, count: int, **kwargs) -> None:
        with allure.step(f"Checking {self.type_of} count value"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_count(count)