# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:43:54 2024.

@author: Archik
"""

import pandas as pd
# import numpy as np

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv("D:\\Python\\MLCourse\\ml-100k\\u.data", sep='\t',
                      names=r_cols, usecols=range(3), encoding='ISO-8859-1')
m_cols = ['movie_id', 'title']
movies = pd.read_csv("D:\\Python\\MLCourse\\ml-100k\\u.item", sep='|',
                     names=m_cols, usecols=range(2), encoding='ISO-8859-1')
ratings = pd.merge(movies, ratings)
ratings.head()

movie_ratings = ratings.pivot_table(index=['user_id'], columns=['title'],
                                    values='rating')
movie_ratings.head()
starwars_ratings = movie_ratings['Star Wars (1977)']
starwars_ratings.head()

similar_movies = movie_ratings.corrwith(starwars_ratings)
similar_movies = similar_movies.dropna()
df = pd.DataFrame(similar_movies)
df.head(10)

similar_movies.sort_values(ascending=False)

movie_stats = ratings.groupby('title').agg({'rating': ['size', 'mean']})
movie_stats.head()

popular_movies = movie_stats['rating']['size'] >= 150
movie_stats[popular_movies].sort_values([('rating', 'mean')],
                                        ascending=False)[:15]
mapped_column_moviestat = movie_stats[popular_movies]
mapped_column_moviestat.columns = [f"{i}|{j}" if j != '' else f'{i}'
                                   for i, j in mapped_column_moviestat.columns]
df = mapped_column_moviestat.join(pd.DataFrame(similar_movies,
                                               columns=['Similarity']))
df.head()
X = df.sort_values(['Similarity'], ascending=False)[:15]
print(X)
