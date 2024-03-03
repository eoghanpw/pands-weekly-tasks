# weekday
# program that outputs whether or not today is a weekday
# author: eoghan walsh
# ref: https://www.w3schools.com/python/python_datetime.asp

import datetime

today = datetime.datetime.today()

if today.strftime("%A") == "Saturday" or "Sunday":
    print("Yay, it's the weekend!")

else:
    print("Unfortunately today is a weekday. Boo!")

