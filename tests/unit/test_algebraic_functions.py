import os
import sys

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from src.utils import add, subtract, multiply, divide

class TestCalculator:
    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)

    def test_multiplication(self):
        assert 6 == multiply(2, 3)

    def test_division(self):
        assert 3 == divide(6, 2)
        assert "Error: Division by zero is undefined." == divide(5, 0)
