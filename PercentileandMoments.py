# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:48:00 2024.

@author: Archik
"""

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt
from pylab import randn


vals = np.random.normal(0, 0.5, 10000)
np.percentile(vals, 50)
# First moment
print(f"Mean: {np.mean(vals)}")
# Second moment
print(f"Variance: {np.var(vals)}")
# Third moment
print(f"Skew: {sp.skew(vals)}")
# Fourth moment
print(f"Kurtosis: {sp.kurtosis(vals)}")

# Some important points on matplotlib.pyplot
x = np.arange(-3, 3, 0.001)
plt.plot(x, sp.norm.pdf(x))  # Simple

# Double graphs
x = np.arange(-3, 3, 0.001)
plt.plot(x, sp.norm.pdf(x))
plt.plot(x, sp.norm.pdf(x, 1.0, 0.5))

# Save a file
plt.savefig("D:\\Python\\Myplot.png", format='png')

# Adjust axes
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
# Setting tick marks
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.plot(x, sp.norm.pdf(x))
plt.plot(x, sp.norm.pdf(x, 1.0, 0.5))
plt.show()
# Add grid
axes = plt.axes()
axes.grid()
# Labelling Axes and Adding legends
plt.xlabel("Greebles")
plt.ylabel("Probability")
plt.legend(['Sneetches', 'Gacks'], loc=4)
# Change line types and colors
plt.plot(x, sp.norm.pdf(x), 'b-')
plt.plot(x, sp.norm.pdf(x, 1.0, 0.5), 'r:')
plt.show()
# xkcd
plt.xkcd()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')
ax.set_ylim([-30, 10])
data = np.ones(100)
data[70:] -= np.arange(30)
plt.annotate("The Day I realised\n"
             "I could cook\n"
             "Whenever I wanted\n", xy=(70, 1),
             arrowprops=dict(arrowstyle='->'),
             xytext=(15, -11)
             )
plt.plot(data)
plt.rcdefaults()  # Remove xkcd mode
# Pie chart
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0]
Labels = ['India', 'USA', 'Russia', 'China', 'Europe']
plt.pie(values, colors=colors, labels=Labels, explode=explode)
plt.title('Student Locations')
plt.show()
# Bar Chart (Similar to pie chart)
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0, 5), values)
plt.show()
# Scatter plot
X = randn(500)
Y = randn(500)
plt.scatter(X, Y)
plt.show()
# Histogram
income = np.random.normal(27000, 15000, 10000)
plt.hist(income, 50)
plt.show()
# Box and Wisker plot
# Box represent where 50% of date resides
# and whiskers where other 25% resides on
# each side except outliers, We define outliers as anything
# beyond 1.5 times the inter quartile range (or size of box)
uniformskewed = np.random.rand(100)
highoutliers = np.random.rand(10)
lowoutliers = np.random.rand(10)
data = np.concatenate((uniformskewed, highoutliers, lowoutliers))
plt.boxplot(data)
plt.show()
