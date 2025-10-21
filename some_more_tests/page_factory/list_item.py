from some_more_tests.page_factory.component_base import Component

class ListItem(Component):

    @property
    def type_of(self) -> str:
        return "class"