# bank.py
# This program prompts the user and reads in two money amounts (in cent),
# then adds the two amounts and prints out the answer in readable format with Euro sign and decimal point.
# Author: Eoghan Walsh

amount1 = int(input('Enter amount1(in cent): '))
amount2 = int(input('Enter amount2(in cent): '))
amount3 = (amount1 + amount2) / 100
amount4 = "{:,.2f}".format(amount3) # formats number to 2 decimal places and adds thousands separator. Reference: https://pythonguides.com/python-format-number-with-commas/
print(f'The sum of these is €{amount4}')