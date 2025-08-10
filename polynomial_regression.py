# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:05:07 2024.

@author: Archik
"""

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from sklearn.metrics import r2_score

np.random.seed(2)
page_speeds = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 10.0, 1000) / page_speeds

pl.scatter(page_speeds, purchase_amount)
x = np.array(page_speeds)
y = np.array(purchase_amount)
p4 = np.poly1d(np.polyfit(x, y, 8))

xp = np.linspace(0, 7, 100)
plt.scatter(xp, p4(xp), c='r')
plt.show()

r2 = r2_score(y, p4(x))
print(r2)
