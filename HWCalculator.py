# Task: Create a Calculator

# Your task is to create a basic calculator program using Python.

# The program should allow the user to perform simple arithmetic operations on two numbers.

# Requirements:

# Prompt the user to enter two numbers.
# Prompt the user to select an operation from the following options:
# addition
# subtraction
# multiplication
# division.

# Based on the selected operation, perform the corresponding calculation. Display the result to the user.

# Note:

# Ensure that the program handles division by zero and provides an appropriate error message if the user attempts to divide by zero.
# Consider using functions to encapsulate the calculation logic for each operation.
# Include clear instructions and error handling for invalid input.


print("Welcome to the Calculator Program!")
next_operation = 'y'
while next_operation == 'y':
    number1 = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))
    operation = input("Please select an operation: +, -, *, /: ")
    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation == '*':
        print(number1 * number2)
    elif operation == '/':
        print(number1 / number2 if number2 >
              0 else "Error. You cant divide by zero. Please select another operation")
    else:
        print("Error. There is no such operation. Please select another operation")
    next_operation = input("Press 'y' to continue: ")
input()
