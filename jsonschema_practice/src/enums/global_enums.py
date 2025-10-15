from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Response status is not equal to what expected"
    WRONG_COUNT = "Response count is not equal to what expected"