# accounts2.py
# program that reads in an account number of any length and outputs the account number with all but the last four digits relaced with Xs.
# author: eoghan walsh
# ref: https://www.w3schools.com/python/python_conditions.asp
# assumptions:
#   1. If account number is one digit in length output will be X.
#   2. If length of account number greater than 1 and less than 8 digits, program will replace at least half of first digits with X.(half for even, rounded up for odd)
#   3. If length of account 8 digits or more, program will replace all but last four digits with X.


ac_number = input("Please enter an account number: ")
length_ac_number = len(ac_number)
short_ac_number = int(length_ac_number / 2)
secure_short_ac_number = ac_number.replace(ac_number[:-short_ac_number],"X"*(length_ac_number - short_ac_number))
secure_long_ac_number = ac_number.replace(ac_number[:-4],"X"*(length_ac_number - 4))

if length_ac_number == 1:
    print("X")

if length_ac_number >1 and length_ac_number <8:
    print(secure_short_ac_number)

if length_ac_number >=8:
    print(secure_long_ac_number)