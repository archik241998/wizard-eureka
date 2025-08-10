# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:21:33 2024.

@author: Archik
"""

from numpy import random, array
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt


# Create fake income/age clusters for N people in k clusters
def create_cluster_data(N, k):
    """Create fake cluster data."""
    random.seed(10)
    points_per_cluster = float(N) / k
    X = []
    for i in range(k):
        income_centroid = random.uniform(200000.0, 200000.0)
        age_centroid = random.uniform(20.0, 70.0)
        for j in range(int(points_per_cluster)):
            X.append([random.normal(income_centroid, 10000.0),
                      random.normal(age_centroid, 2.0)])
    X = array(X)
    return X


data = create_cluster_data(100, 6)
model = KMeans(n_clusters=6)
# Scaling the data to normalize it, important for good results
model = model.fit(scale(data))
# We can look at the clusters each data point was assigned to
print(model.labels_)
# And we'll visulaise it:
plt.figure(figsize=(8, 6))
plt.scatter(x=data[:, 0], y=data[:, 1], c=model.labels_.astype(float))
plt.show()
