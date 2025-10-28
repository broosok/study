import allure

from some_more_tests.page_factory.component_base import Component


class Uploader(Component):

    @property
    def type_of(self) -> str:
        return "uploader"

    def upload(self, file_path: str, **kwargs) -> None:
        with allure.step(f"Uploading {file_path} to {self.type_of}"):
            locator = self.get_locator(**kwargs)
            locator.set_input_files(file_path)