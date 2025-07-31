# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

def safe_divide(num1, num2):
    """Returns a safe division or an error message."""
    try:
        result = num1 / num2
        return f"The result of {int(num1)} divided by {int(num2)} is {int(result)}."
    except ZeroDivisionError:
        return "Error: You cannot divide by zero. Please enter a non-zero denominator."

def divide_numbers():
    """Handles user input/output."""
    try:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        message = safe_divide(num1, num2)
        print(message)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    divide_numbers()