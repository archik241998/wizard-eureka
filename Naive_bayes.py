# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:32:40 2024.

@author: Archik
"""

import os
import io
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def readfiles(path):
    """Read files as dataframe."""
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            inbody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inbody:
                    lines.append(line)
                elif line == '\n':
                    inbody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataframe_from_directory(path, classification):
    """Return dataframe from path."""
    rows = []
    index = []
    for filename, message in readfiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(classification)
    return DataFrame(rows, index=index)


data = DataFrame({'message': [], 'class': []})
data = pd.concat([data,
                 dataframe_from_directory('D:\\Python\\MLCourse\\emails\\spam',
                                          'spam')])
data = pd.concat([data,
                  dataframe_from_directory('D:\\Python\\MLCourse\\emails\\ham',
                                           'ham')])
data.head()
vectorizer = CountVectorizer()
count = vectorizer.fit_transform(data['message'].values)
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(count, targets)

examples = ['Free Viagra now !!!!',
            'Hi Bob, how about a game of golf tomorrow?']
examples_counts = vectorizer.transform(examples)
predictions = classifier.predict(examples_counts)
print(predictions)
