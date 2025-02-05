import pytest
import string

class Calculator:

    NO_STRING = "Debe ingresar un string"

    def __init__(self, numbers):
        self.numbers = numbers
    
    @classmethod
    def add(self, numbers):
        if numbers == "":
            return self.NO_STRING


def test_empty_string():
    calculator = Calculator(
        numbers = ""
    )
    assert calculator.numbers == ""
    return calculator.NO_STRING
