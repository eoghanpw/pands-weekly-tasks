# Weekly Task 5: weekday.py
# Program that outputs whether or not today is the weekend.
# Author: Eoghan Walsh
# ref: https://www.w3schools.com/python/python_datetime.asp

# Import the datetime module.
import datetime

# Get the current date.
today = datetime.datetime.today()

# Format date to weekday string.
weekday = today.strftime("%A")

# Print response based on weekday.
if weekday == "Saturday" or "Sunday":
    print("Yay, it's the weekend!")

else:
    print("Unfortunately today is a weekday. Boo!")
