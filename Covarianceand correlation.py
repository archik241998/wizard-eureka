# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:56:44 2024.

@author: Archik
"""
import numpy as np
import seaborn as sns


def de_mean(x):
    """Return the list of difference with mean."""
    xmean = np.mean(x)
    return [xi - xmean for xi in x]


def covariance(x, y):
    """Return covarriance between x and y."""
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)


def correlation(x, y):
    """Return correlation between x and y."""
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x, y) / stddevx / stddevy
# In real life you'd check for divide by zero here


pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 10.0, 100)
sns.scatterplot(x=pageSpeeds, y=purchaseAmount)
print(covariance(pageSpeeds, purchaseAmount))

print(correlation(pageSpeeds, purchaseAmount))

purchaseAmount = np.random.normal(50.0, 10.0, 100) / pageSpeeds
sns.scatterplot(x=pageSpeeds, y=purchaseAmount)
print(covariance(pageSpeeds, purchaseAmount))

print(np.corrcoef(pageSpeeds, purchaseAmount))

purchaseAmount = 100 - pageSpeeds * 3
sns.scatterplot(x=pageSpeeds, y=purchaseAmount)
print(correlation(pageSpeeds, purchaseAmount))
