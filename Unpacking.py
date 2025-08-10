# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:03:31 2024

@author: Archik
"""

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad COmpany", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))
for album in albums:
    print(len(album))
    for i in enumerate(album):
        song, artist, year = album[0], album[1], album[2]
    print((song, artist, year))
