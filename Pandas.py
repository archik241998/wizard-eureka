# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:41:26 2024.

@author: Archik
"""
# import numpy as np
import pandas as pd

df = pd.read_csv("D:\\Python\\MLCourse\\PastHires.csv")  # Read csv files
df.head()
q = df.head(10)  # First 10 rows of the data frame.
t = df.tail(4)  # Last 4 rows of the data frame.
print(df.shape)  # Rows and columns
print(df.size)  # Rows x columns
print(len(df))  # Number of rows
print(df.columns)  # Array of column names
print(df["Hired"])  # to extract single column from dataframe
print(df["Hired"][5])  # Extract a single value
print(df[["Years Experience", "Hired"]][:5])  # for more than one columns
print(df.sort_values(["Years Experience"]))
# Break down number of unique values in a given column into series
degree_count = df["Level of Education"].value_counts()
print(degree_count)
# Pandas even makes it easy to plot a series or data frames.
print(degree_count.plot(kind='bar'))
