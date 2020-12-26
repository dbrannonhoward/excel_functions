class CommonFunctions:
    def __init__(self):
        pass

    def add_two_integers(self, a: int, b: int) -> int:
        if self.is_integer(a) and self.is_integer(b):
            print(str(a) + " plus " + str(b) + " is " + str(a + b))
            return a + b

    def add_two_strings(self, a: str, b: str) -> str:
        if self.is_string(a) and self.is_string(b):
            print(str(a) + " plus " + str(b) + " is " + str(a + b))
            return a + b

    def is_integer(self, variable_to_test) -> bool:
        if isinstance(variable_to_test, int):
            return True
        return False

    def is_string(self, variable_to_test) -> bool:
        if isinstance(variable_to_test, str):
            return True
        return False

class TestCode:
    def __init__(self):
        pass

    def main_test_sequence(self):
        cf = CommonFunctions()
        cf.add_two_integers(85, 342)
        cf.add_two_strings('potato', 'cat')

tc = TestCode()
tc.main_test_sequence()
pass