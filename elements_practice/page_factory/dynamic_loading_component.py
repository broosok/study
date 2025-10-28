import allure
from playwright.sync_api import expect

from some_more_tests.page_factory.component_base import Component

class DynamicLoadingComponent(Component):

    @property
    def type_of(self) -> str:
        return "dynamic loading component"

    def click_start_loading_button(self, **kwargs) -> None:
        with allure.step(f"Clicking start loading button for {self.type_of}"):
            locator = self.get_locator(**kwargs)
            locator.click()

    def wait_for_loading(self, text: str, timeout: int = 30000, **kwargs) -> None:
        with allure.step(f"Waiting for loading {self.type_of} to load"):
            locator = self.get_locator(**kwargs)
            locator.wait_for(state="visible", timeout=timeout)
            expect(locator).to_contain_text(text)