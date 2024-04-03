# plottask.py
#
# program that displays a histogram of a normal distribution 
#   of a 1000 values with a mean of 5 and standard deviation of 2, 
#   and a plot of the function h(x)=x^3 in the range 0 to 10, 
#   on the one set of axes.
#
# author: eoghan walsh
#
# references: https://www.w3schools.com/python/matplotlib_histograms.asp

import numpy as np
import matplotlib.pyplot as plt

hist_mean =  5
hist_std_dev = 2
hist_size = 1000

x = np.random.normal(hist_mean, hist_std_dev, hist_size)

plt.hist(x)
plt.show()

