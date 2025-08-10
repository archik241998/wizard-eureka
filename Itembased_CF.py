# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:53:10 2024.

@author: Archik
"""

import pandas as pd


r_cols = ['User_id', 'Movie_id', 'Rating']
ratings = pd.read_csv("D:\\Python\\MLCourse\\ml-100k\\u.data", sep='\t',
                      names=r_cols, usecols=range(3), encoding='ISO-8859-1')
m_cols = ['Movie_id', 'Title']
movies = pd.read_csv("D:\\Python\\MLCourse\\ml-100k\\u.item", sep='|',
                     names=m_cols, usecols=range(2), encoding='ISO-8859-1')
ratings = pd.merge(movies, ratings)
ratings.head()

user_rating = ratings.pivot_table(index=['User_id'], columns=['Title'],
                                  values='Rating')
user_rating.head()

"""Now the magic happens - pandas has a built-in corr() method that
will compute a correlation score for every column pair in the matrix!
This gives us a correlation score between every pair of movies
(where at least one user rated both movies - otherwise NaN's will show up.)"""

corr_matrix = user_rating.corr()
corr_matrix.head()

corr_matrix = user_rating.corr(method='kendall', min_periods=80)
corr_matrix.head()

my_rating = user_rating.loc[0].dropna()
print(my_rating)

# For recommendations we'll create a dummy candidate
sim_candidate = pd.Series()

for i in range(0, len(my_rating.index)):
    print("Adding sims for my rating" + my_rating.index[i] + "...")
    # Retrieve similar movie to the one we rated
    sim = corr_matrix[my_rating.index[i]].dropna()
    # Now scale its similarity by how well we rated this movie
    sim = sim.map(lambda x: x * my_rating[i])
    # Adding score to the list of similarity candidates
    sim_candidate = pd.concat([sim_candidate, sim])

print("Sorting...")
sim_candidate.sort_values(inplace=True, ascending=False)
print(sim_candidate.head(10))

sim_candidate = sim_candidate.groupby(sim_candidate.index).sum()
sim_candidate.sort_values(inplace=True, ascending=False)
sim_candidate.head(10)

filtered_sim = sim_candidate.drop(my_rating.index)
filtered_sim.head(10)
