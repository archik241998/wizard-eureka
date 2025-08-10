# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:28:41 2024.

@author: Archik
"""
import sklearn.preprocessing as skp
import numpy as np
import matplotlib.pyplot as plt
import librosa
arr = []
x, sr = librosa.load("D:\\Python\\SpeechModel\\male.wav", sr=None)
print(x)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(np.abs(X))
print('X: ', Xdb)
plt.figure(figsize=(20, 10))
# librosa.display.waveshow(Xdb, axis='s', where='mid')
# librosa.display.specshow(Xdb)
s = 22050
T = 0.5
# t = np.linspace(0, T, int(T*s), endpoint=False)
# print('t:', t)
# w = 0.5*np.sin(2*np.pi*220*t)  # pure sin wave at 220 Hz
# Normalising
n_fft = 2048
hop_length = 512

spec = np.abs(librosa.core.stft(x, n_fft=n_fft, hop_length=hop_length))
freqs = librosa.core.fft_frequencies(n_fft=n_fft)
times = librosa.core.frames_to_time(spec[0], sr=s,
                                    n_fft=n_fft, hop_length=hop_length)
t = times
print('t: ', t)

# librosa.display.waveshow(w, sr=s)
wdb = skp.scale(Xdb, with_mean=0)
librosa.display.waveshow(wdb, axis='s', where='mid')
# plt.plot_date(wdb, t)
