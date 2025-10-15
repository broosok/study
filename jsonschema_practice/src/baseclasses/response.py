from jsonschema import validate
from ..enums.global_enums import GlobalErrorMessages

class Response:
    def __init__(self, response):
        self.response = response
        self.json = response.json()
        self.response_status = response.status_code

    def validate_schema(self, schema):

        if isinstance(self.json, list):
            for item in self.json:
                validate(item, schema)
        else:
            validate(self.json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value()
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value()
        return self