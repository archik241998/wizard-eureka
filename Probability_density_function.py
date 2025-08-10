# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:18:17 2024.

@author: Archik
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson


values = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(values, 50)

x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))

# for discrete Normal Distribution
values = np.random.normal(30, 20, 10000)
plt.hist(values, 50)
plt.show()

# For exponential PDF or power law
x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))

# for Binomial Mass distribution
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))

# Poisson's Probability Mass function
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
