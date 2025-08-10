# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:08:05 2024

@author: Archik
"""

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for i in range(1, len(data)+1):
    if 'Flower' in data[i-1]:
        flowers.append(data[i-1])
    else:
        shrubs.append(data[i-1])
    
print(flowers)
print(shrubs)