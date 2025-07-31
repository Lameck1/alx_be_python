# Create a custom exception class called ValueTooHighError that inherits from the Exception class.
# Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

class ValueTooHighError(Exception):
    """Custom exception raised when a value exceeds the allowed limit."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Value {value} is too high! It must be 100 or less.")

def check_value(value):
    if value > 100:
        raise ValueTooHighError(value)
    else:
        print(f"Value {value} is within the allowed range.")

if __name__ == "__main__":
    try:
        user_input = float(input("Enter a number: "))
        check_value(user_input)
    except ValueTooHighError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
