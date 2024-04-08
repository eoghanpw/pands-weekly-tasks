# Weekly Task 7: es.py
# Program that reads in a text file and outputs
# the number of e's it contains.
# Author: Eoghan Walsh

# Import sys.
import sys

# Import os.path.
import os.path

# Filename can be input on command line.
try:
    FILENAME = sys.argv[1]
except IndexError:
    print("Please enter filename.")
    sys.exit(1)


# Function to count the occurances of the letter e in the file.
def e_count():
    with open(FILENAME) as f:
        str = f.read()
        count = str.count("e") + str.count("E")
        print(count)


if not os.path.isfile(FILENAME):
    print("File does not exist.")
elif ".txt" not in FILENAME:
    print("File extension not valid. Please select .txt file.")
else:
    e_count()
