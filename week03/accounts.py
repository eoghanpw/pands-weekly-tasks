# Weekly Task 3: accounts.py
# Program that reads in a 10 character account number
# and outputs the account number with first 6 characters replaced with Xs.
# Author: Eoghan walsh

# Prompt user to input account number.
ac_number = (input("Please enter a 10 digit account number: "))

# If not 10 characters, will prompt user to input account number again.
while len(ac_number) != 10:
    ac_number = (input("Please enter a 10 digit account number: "))

# Replace first 6 characters with Xs.
secure_ac_number = ac_number.replace(ac_number[:-4], "XXXXXX")

print(secure_ac_number)
