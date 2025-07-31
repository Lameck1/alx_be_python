import unittest
from custom_value_too_error import check_value, ValueTooHighError

class TestCheckValue(unittest.TestCase):

    def test_value_within_limit(self):
        # Should not raise an exception
        try:
            check_value(50)  # value <= 100
        except Exception:
            self.fail("check_value() raised an exception for a valid value")

    def test_value_exactly_at_limit(self):
        # Should also be accepted
        try:
            check_value(100)
        except Exception:
            self.fail("check_value() raised an exception for value 100")

    def test_value_above_limit_raises_custom_error(self):
        # Should raise ValueTooHighError
        with self.assertRaises(ValueTooHighError) as context:
            check_value(150)
        self.assertEqual(str(context.exception), "Value 150 is too high! It must be 100 or less.")

if __name__ == "__main__":
    unittest.main()
