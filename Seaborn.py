# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:21:15 2024.

@author: Archik
"""

import pandas as pd
import seaborn as sns


df = pd.read_csv("D:\\Python\\MLCourse\\FuelEfficiency.csv")
df.head()
gear_counts = df["# Gears"].value_counts()
gear_counts.plot(kind='bar')
# distplot/histplot
sns.displot(df["CombMPG"], kde=True)
# Pairplot
df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]
df2.head()
sns.pairplot(df2, hue='Cylinders', height=2.5)
sns.scatterplot(x="Eng Displ", y="CombMPG", data=df)  # Scatterplot
sns.jointplot(x="Eng Displ", y="CombMPG", data=df)  # Jointplot
sns.lmplot(x="Eng Displ", y="CombMPG", data=df)  # lmplot
# Boxplot
sns.set(rc={'figure.figsize': (15, 5)})
ax = sns.boxplot(x='Mfr Name', y='CombMPG', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
# Swarmplot
ax = sns.swarmplot(x='Mfr Name', y='CombMPG', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
# Countplot
ax = sns.countplot(x='Mfr Name', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
# Heatmap
df2 = df.pivot_table(index='Cylinders', columns='Eng Displ',
                     values='CombMPG', aggfunc='mean')
sns.heatmap(df2)
