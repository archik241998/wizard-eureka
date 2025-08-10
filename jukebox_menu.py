# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:33:53 2024

@author: Archik
"""
from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album:")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{} : {}".format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONGS_LIST_INDEX]
    else:
        choice = int(input("Please choose your album:"))
    print("PLease choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{} : {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice -1][SONG_TITLE_INDEX]
    else:
        #song_choice = int(input("PLease choose your song:"))
        break
    print("Now playing {}".format(title))
    print("=" * 40)