# Weekly Task 8: plottask.py
# Program that displays a histogram of a normal distribution
# of 1000 values with a mean of 5 and standard deviation of 2,
# and a plot of the function h(x)=x^3 in the range 0 to 10,
# on the one set of axes.
# Author: Eoghan Walsh

# Import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

# Set normal distribution parameters.
hist_mean = 5
hist_std_dev = 2
hist_size = 1000

# Use numpy random.normal() to generate normal data distribution.
norm_dist = np.random.normal(hist_mean, hist_std_dev, hist_size)

# Set range for x.
x_range_low = 0
x_range_high = 10

# Use numpy to generate array for x.
x = np.array(range(x_range_low, x_range_high))

# X cubed function: h(x) = x^3
x_cubed = x * x * x

# Plot histogram of normal distribution and add label.
plt.hist(norm_dist, label="Normal Distribution")

# Plot x cubed function and add label.
plt.plot(x, x_cubed, label="$h(x)=x^3$")

# Add legend to plot
plt.legend()

# Add title to plot
plt.title("Weekly Task 8: plottask.py")

# Show the plot
plt.show()
