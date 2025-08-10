# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 00:28:41 2024.

@author: Archik
"""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
pagespeed = np.random.normal(3.0,  1.0, 100)
purchase_amount = np.random.normal(50.0, 30.0, 100) / pagespeed
pl.scatter(pagespeed, purchase_amount)

train_x = pagespeed[:80]
test_x = pagespeed[80:]
train_y = purchase_amount[:80]
test_y = purchase_amount[80:]
pl.scatter(train_x, train_y)
pl.show()
pl.scatter(test_x, test_y)
pl.show()

x = np.array(train_x)
y = np.array(train_y)
p4 = np.poly1d(np.polyfit(x, y, 6))

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.show()
plt.plot(xp, p4(xp), c='r')
plt.show()

testx = np.array(test_x)
testy = np.array(test_y)

axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')
plt.show()

r2 = r2_score(testy, p4(testx))
print('r2:', r2)
rsq = r2_score(y, p4(x))
print('rsq:', rsq)
