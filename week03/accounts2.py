# Weekly Task 3: accounts2.py
# Program that reads in an account number of any length
# and outputs the account number based on below assumptions.
# Assumptions:
#   1. If account number is one character in length output will be X.
#   2. If length is greater than 1 and less than 10 (short_ac_number),
#      program will replace at least half of first digits with X.
#   3. If length is 10 or more (long_ac_number), program will replace
#      all but last four digits with X.
# Author: Eoghan Walsh

# Prompt user to input account number.
ac_number = input("Please enter an account number: ")

# Get length of number.
length_ac_number = len(ac_number)

# Slice the ending characters from account numbers.
short_ac_number = ac_number[-(length_ac_number // 2):]

long_ac_number = ac_number[-4:]

# Get number of Xs to use.
short_x = "X"*(length_ac_number - len(short_ac_number))

long_x = "X"*(length_ac_number - 4)

# Create secure account numbers.
secure_short_ac_number = f"{short_x}{short_ac_number}"

secure_long_ac_number = f"{long_x}{long_ac_number}"

# Print secure account number based on length.
if length_ac_number == 1:
    print("X")

if length_ac_number > 1 and length_ac_number < 10:
    print(secure_short_ac_number)

if length_ac_number >= 10:
    print(secure_long_ac_number)
