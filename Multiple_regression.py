# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:28:00 2024.

@author: Archik
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("D:\\Python\\MLCourse\\cars.xls")
df1 = df[['Mileage', 'Price']]
bins = np.arange(0, 50000, 10000)
groups = df1.groupby(pd.cut(df1['Mileage'], bins), observed=True).mean()
print('Group: ', groups.head())
groups['Price'].plot.line()

scale = StandardScaler()
x = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']
x = scale.fit_transform(x.values)
# Add a constant column to our model so we have a y-intercept
X = sm.add_constant(x)
print('X: ', X)
est = sm.OLS(y, X).fit()
print('Sumary: ', est.summary())
print('Y: ', y.groupby(df.Doors).mean())
scaled = scale.transform([[45000, 8, 4]])
scaled = np.insert(scaled[0], 0, 1)  # Need to add thatconstant column in again
print('scale: ', scaled)
predicted = est.predict(scaled)
print('Predicted: ', predicted)
