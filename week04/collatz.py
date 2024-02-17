# collatz.py
# program that asks the user to input any positive ineger
#   and outputs the successive values of the following calc:
#       the next value takes the current value and, if it is even, 
#       divide it by two, but if it is odd, multiply it by three and add one.
#   the program ends when the current value is one.
# author: eoghan walsh

numbers = []

number = int(input("Please enter a positive integer: "))

while number < 1:
    number = int(input("Invalid number. Please enter positive integer: "))

while number != 1:
    numbers.append(number)

    if (number % 2) == 0:
        number = (number / 2)

    else:
        number = (number * 3) + 1
    
numbers.append(number)
number = number / 2

numbers_output = ["{:.0f}".format(number) for number in numbers]

print(*numbers_output)