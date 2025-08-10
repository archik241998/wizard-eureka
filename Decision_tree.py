# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 00:56:38 2024

@author: Archik
"""

import numpy as np
import pandas as pd
from sklearn import tree
from IPython.display import Image
from io import StringIO
import pydotplus
from sklearn.ensemble import RandomForestClassifier

input_file = "D:\\Python\\MLCourse\\PastHires.csv"
df = pd.read_csv(input_file, header=0)
df.head()

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
df.head()

features = list(df.columns[:6])
print('Features: ', features)
y = df['Hired']
x = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
plt = Image(graph.create_png())
display(plt)
clf1 = RandomForestClassifier(n_estimators=10)
clf1 = clf1.fit(x, y)
# Predict employment of an employed 10-year veteran
print(clf1.predict([[10, 1, 4, 0, 0, 0]]))
# ... and an unemployed 10-year veteran
print(clf1.predict([[10, 0, 4, 0, 0, 0]]))
