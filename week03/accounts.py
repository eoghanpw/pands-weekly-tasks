# accounts.py
# program that reads in a 10 character account number and outputs the account number with first 6 digits replaced with X's.
# author: eoghan walsh
# ref: https://www.w3schools.com/python/ref_string_replace.asp

ac_number = input("Please enter a 10 digit account number: ")
secure_ac_number = ac_number.replace(ac_number[:-4],"XXXXXX")
print(secure_ac_number)