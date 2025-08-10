# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:58:45 2024.

@author: Archik
"""

from gtts import gTTS
from PyPDF2 import PdfReader
import os


def pdf_to_text(pdf_file):
    """Create a text-list from pdf file."""
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def text_to_audio(text, output_file):
    """Convert text to audio and save the aus=dio file."""
    tts = gTTS(text)
    tts.save(output_file)


pdf_file = input("Which file to save: ")
output_audio_file = input("Where to save the file: ")

text = pdf_to_text(pdf_file)
text_to_audio(text, output_audio_file)
os.system(output_audio_file)
