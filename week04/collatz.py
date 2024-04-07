# Weekly Task 4: collatz.py
# Program that prompts the user to input any positive integer and outputs
# a list of successive values where each value is obtained from the previous
# as follows:
#   If the previous value is even, the next value is one half of the previous.
#   If the previous value is odd, the next value is 3 times the previous
#   value plus 1.
# The program ends when the next value calculated is one.
# Author: Eoghan Walsh

# Create the list of numbers.
numbers = []

# Prompt user to input number.
number = int(input("Please enter a positive integer: "))

# Prompt user again if number less than 1 input.
while number < 1:
    number = int(input("Invalid number. Please enter positive integer: "))

# Add values to list until number is 1.
while number != 1:
    numbers.append(number)

# Divide even numbers by 2.
    if (number % 2) == 0:
        number = (number // 2)

# Multiply odd numbers by 3 and add 1.
    else:
        number = (number * 3) + 1

# Add value 1 to the end of list.
numbers.append(1)

# Print list without brackets and commas.
print(*numbers)
