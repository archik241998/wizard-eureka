# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:38:27 2024.

@author: Archik
"""

import numpy as np
import pylab as pl
from scipy import stats
import matplotlib.pyplot as plt

page_speeds = np.random.normal(3.0, 1.0, 1000)
purchase_amount = 100 - (page_speeds + np.random.normal(0, 1.0, 1000)) * 3

pl.scatter(page_speeds, purchase_amount)

m, c, r_value, p_value, std_err = stats.linregress(page_speeds,
                                                   purchase_amount)
R = r_value ** 2
print(R)


def predict(x):
    """Return regression line."""
    return m * x + c


fitline = predict(page_speeds)
plt.scatter(page_speeds, purchase_amount)
plt.plot(page_speeds, fitline, c='r')
plt.show()
