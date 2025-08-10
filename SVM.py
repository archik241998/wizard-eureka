# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:48:05 2024.

@author: Archik
"""

import numpy as np
from pylab import*
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm
import matplotlib.pyplot as plt


# Create fake income/age clusters for N people in k
def create_cluster_data(N, k):
    """Create fake cluster data."""
    np.random.seed(10)
    points_per_cluster = float(N) / k
    X = []
    y = []
    for i in range(k):
        income_centroid = np.random.uniform(200000.0, 200000.0)
        age_centroid = np.random.uniform(20.0, 70.0)
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 10000.0),
                      np.random.normal(age_centroid, 2.0)])
            y.append(i)
    y = np.array(y)
    X = np.array(X)
    return X, y


(X, y) = create_cluster_data(100, 5)
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y.astype(float))
plt.show()

scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X)
X = scaling.transform(X)
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y.astype(float))
plt.show()

C = 1.0
svc = svm.SVC(kernel='poly', C=C).fit(X, y)


def plot_predictions(clf):
    """Create a dense grid of points to sample."""
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.001),
                         np.arange(-1, 1, 0.001))
    """Convert to numpy arrays."""
    npx = xx.ravel()
    npy = yy.ravel()

    """Convert to a list of 2D (income, age) points."""
    sample_points = np.c_[npx, npy]

    """Generate Predicted labels (cluster numbers) for each point"""
    z = clf.predict(sample_points)

    plt.figure(figsize=(8, 6))
    z = z.reshape(xx.shape)  # Reshape results to match xx dimension

    # Draw the contours
    plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y.astype(float))  # Draw the points
    plt.show()


plot_predictions(svc)
print(svc.predict(scaling.transform([[200000, 40]])))
print(svc.predict(scaling.transform([[50000, 65]])))
