# Task Advanced: Create a Password Generator for Linux Users

# Your task is to create a password generator program using Python specifically designed for Linux users.
#     The program should generate strong and secure passwords that can be used for user accounts on Linux systems.

# Requirements:

# Prompt the user to enter the desired length for the password.
# Generate a random password consisting of a combination of uppercase letters, lowercase letters, numbers, and special characters.
# Ensure that the generated password meets the following criteria:

# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one number
# Contains at least one special character (e.g., !, @, #, $, %, etc.)
# Display the generated password to the user.

# Note:

# You can utilize the random module in Python to generate random characters and build the password.
# Consider using the string module in Python to access sets of characters (uppercase, lowercase, numbers, and special characters).
# Make sure to include clear instructions and error handling for invalid input.

import string
import random

print("Welcome to the Linux User Password Generator!")

upper = string.ascii_uppercase
lower = string.ascii_lowercase
number = string.digits
special = string.punctuation
allsymb = upper + lower + number + special
password = ""

length = int(input("Please enter the desired password length: "))

if upper:
    allsymb += upper
if lower:
    allsymb += lower
if number:
    allsymb += number
if special:
    allsymb += special

for x in range(length):
    password = "".join(random.sample(allsymb, length))
print(password)

input()
