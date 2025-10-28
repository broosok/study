import pytest

from elements_practice.components.file_uploader import UploaderPage

class TestUploaderPage:

    @pytest.mark.parametrize('file_path', ['example.jpg'])
    def test_upload(self, uploader_page: UploaderPage, file_path: str) -> None:
        uploader_page.visit("https://the-internet.herokuapp.com/upload")
        uploader_page.uploader.upload(file_path)
