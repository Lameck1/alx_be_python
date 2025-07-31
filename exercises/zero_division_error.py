# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

def divide_numbers():
    try:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        result = num1 / num2
        print(f"The result of {int(num1)} divided by {int(num2)} is {int(result)}.")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero. Please enter a non-zero denominator.")

if __name__ == "__main__":
    divide_numbers()