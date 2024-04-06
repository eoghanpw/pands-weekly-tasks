# Weekly Task 2: bank.py
# This program prompts the user and reads in two money amounts (in cent),
# then adds the two amounts and prints out the answer
# in readable format with Euro sign and decimal point.
# Author: Eoghan Walsh

# Prompt user to input two amounts.
amount1 = int(input('Enter amount1(in cent): '))
amount2 = int(input('Enter amount2(in cent): '))

# Sum the amounts and convert to euro and cent.
sum = (amount1 + amount2) / 100

# Format the number to 2 decimal places and add thousand separator.
formatted_sum = "{:,.2f}".format(sum)

print(f'The sum of these is €{formatted_sum}')
