# plottask.py
#
# program that displays a histogram of a normal distribution 
#   of 1000 values with a mean of 5 and standard deviation of 2, 
#   and a plot of the function h(x)=x^3 in the range 0 to 10, 
#   on the one set of axes.
#
# author: eoghan walsh
#
# references: 
# https://www.w3schools.com/python/matplotlib_histograms.asp
# https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# https://matplotlib.org/stable/users/explain/text/text_intro.html#text-intro

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# set normal distribution parameters
hist_mean =  5
hist_std_dev = 2
hist_size = 1000

# use numpy random.normal() to generate normal data distribution
norm_dist = np.random.normal(hist_mean, hist_std_dev, hist_size)

# set range for x
x_range_low = 0
x_range_high = 10

# use numpy to generate array for x
x = np.array(range(0,10))

# h(x) = x^3
x_cubed = x * x * x

# plot histogram of normal distribution and add label
plt.hist(norm_dist, label = "Normal Distribution")
# plot x cubed and add label
plt.plot(x, x_cubed, label = "$h(x)=x^3$")
# add legend to plot
plt.legend()
# add title to plot
plt.title("Weekly Task 8: plottask.py")
# show the plot
plt.show()