import allure

from some_more_tests.page_factory.component_base import Component

class Link(Component):

    @property
    def type_of(self) -> str:
        return "link"

    # def click(self, **kwargs) -> None:
    #     with allure.step(f"Clicking the {self.type_of} {self.name}"):
    #         locator = self.get_locator(**kwargs)
    #         locator.click()

    