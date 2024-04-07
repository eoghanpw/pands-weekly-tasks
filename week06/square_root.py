# square_root.py
# Program that takes a positive floating-point number as
# an input and outputs an approximation of its square root
# using "Newton's" method to compute square roots.
# Author: Eoghan Walsh

# Define square root function.
def sqrt():
    number = float(input("Please enter a positive number: "))
    # Using 1 as first approxiamtion.
    approx_sqrt = 1
    # Running 50 approximations.
    for x in range(50):
        # Newton's method.
        approx_sqrt = (((number / approx_sqrt) + approx_sqrt) / 2)
    print(f"The square root of {number} is approx. {approx_sqrt}")


# Call function
sqrt()
