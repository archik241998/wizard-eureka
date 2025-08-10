# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 02:12:38 2024.

@author: Archik
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
incomes = np.random.normal(27000, 15000, 10000)
print(f"Mean incomes: {np.mean(incomes)}")  # Check the mean of income chart
plt.hist(incomes, 50)
plt.show()

print(f"Median incomes: {np.median(incomes)}")
income = np.append(incomes, [[10000000]])
print(f"Mean income: {np.mean(income)}")
print(f"Median income: {np.median(income)}")

ages = np.random.randint(18, high=90, size=500)
print(f"Mode ages: {stats.mode(ages)}")

print(f"Standard Deviation: {income.std()}")
print(f"Variance: {income.var()}")
