from enum import Enum


class Environment(str, Enum):
    LOCAL = "LOCAL"
    PROD = "PROD"
    TEST = "TEST"

    @property
    def is_local(self):
        return self == self.LOCAL

    @property
    def is_prod(self):
        return self == self.PROD

    @property
    def is_test(self):
        return self == self.TEST
