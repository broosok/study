import pytest

from elements_practice.components.link_list import LinkPage

class TestLinkListPage:

    @pytest.mark.parametrize('file_name', ['CV Template.docx'])
    def test_dropdown_page(self, linklist_page: LinkPage, file_name: str) -> None:
        linklist_page.visit("https://the-internet.herokuapp.com/download")
        linklist_page.linklist.download(file_name=file_name)