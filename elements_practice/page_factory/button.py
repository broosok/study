import allure

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

