import unittest
from zero_division_error import safe_divide

class TestSafeDivide(unittest.TestCase):

    def test_valid_division(self):
        result = safe_divide(10, 2)
        self.assertEqual(result, "The result of 10 divided by 2 is 5.")

    def test_division_by_zero(self):
        result = safe_divide(10, 0)
        self.assertEqual(result, "Error: You cannot divide by zero. Please enter a non-zero denominator.")

    def test_float_result(self):
        result = safe_divide(9, 2)
        self.assertEqual(result, "The result of 9 divided by 2 is 4.")  # int(4.5) is 4

if __name__ == "__main__":
    unittest.main()