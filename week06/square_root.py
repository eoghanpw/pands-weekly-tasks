# square_root.py

# program that takes a positive floating-point number as
#   an input and outputs an approximation of its square root
#   using "Newton's" method to compute square roots.

# ref1: https://www.youtube.com/watch?v=FpOEx6zFf1o
# ref2: https://www.w3schools.com/python/python_functions.asp
# ref3: https://www.w3schools.com/python/python_for_loops.asp

# author: eoghan walsh

# square root function
def sqrt():
    number = float(input("Please enter a positive number: "))
    approx_sqrt = 1
    for x in range(10):
        approx_sqrt = (((number / approx_sqrt) + approx_sqrt) / 2)
    print(f"The square root of {number} is approx. {approx_sqrt}")

# call function
sqrt()
