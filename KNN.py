# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:39:41 2024.

@author: Archik
"""

import pandas as pd
import numpy as np
from scipy import spatial
import operator


def compute_distance(a, b):
    """Compute distance between two points."""
    genresA = a[1]
    genresB = b[1]
    genre_distance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularity_distance = abs(popularityA - popularityB)
    return genre_distance + popularity_distance


def get_neighbors(movieid, K):
    """Get neighbor distance for KNN."""
    distance = []
    for movie in movie_dict:
        if movie != movieid:
            dist = compute_distance(movie_dict[movieid], movie_dict[movie])
            distance.append((movie, dist))
    distance.sort(key=operator.itemgetter(1))
    neighbor = []
    for x in range(K):
        neighbor.append(distance[x][0])
    return neighbor


r_cols = ['User_id', 'Movieid', 'Rating']
ratings = pd.read_csv("D:\\Python\\MLCourse\\ml-100k\\u.data", sep='\t',
                      names=r_cols, usecols=range(3), encoding='ISO-8859-1')
ratings.head()

movieproperties = ratings.groupby('Movieid').agg({'Rating':
                                                  ['size', 'mean']})
movieproperties.head()

movienumrating = pd.DataFrame(movieproperties['Rating']['size'])
mynormalisedratings = movienumrating.apply(lambda x:
                                           (x - np.min(x)) / (np.max(x) - np.min(x)))
print(mynormalisedratings.head())

movie_dict = {}

with open(r"D:\\Python\\MLCourse\\ml-100k\\u.item",
          encoding='ISO-8859-1') as f:
    temp = ''
    for line in f:
        # line.decode('ISO-8859-1')
        fields = line.rstrip('\n').split('|')
        movieid = int(fields[0])
        name = fields[1]
        genres = fields[5: 25]
        genres = map(int, genres)
        movie_dict[movieid] = (name, np.array(genres),
                               mynormalisedratings.loc[movieid].get('size'),
                               movieproperties.loc[movieid].Rating.get('mean'))

print(movie_dict[1])
print(movie_dict[2])
print(movie_dict[4])

compute_distance(movie_dict[2], movie_dict[4])
K = 20
avg_rating = 0
neighbor = get_neighbors(1, K)
for i in neighbor:
    avg_rating += movie_dict[i][3]
    print(movie_dict[i][0] + ' ' + str(movie_dict[i][3]))

avg_rating /= K

print(avg_rating)
print(movie_dict[1])
