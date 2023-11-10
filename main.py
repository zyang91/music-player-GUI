import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
import os
import pygame
import time
from mutagen.mp3 import MP3

def select_music_folder():
    pass
def previous_song():
    pass
def next_song():
    pass
def play_song():
    pass
def pause_song():
    pass

# establish the main window
window = tk.Tk()
window.title("MP3 Player")
window.geometry("500x500")

#Create label for the music player title
title_music_player = tk.Label(window, text="MP3 Player", font=("Arial", 30))
title_music_player.pack(pady=10)

#create a button to open the file explorer

button_select_folder=ctk.CTkButton(window, text="Select Folder", command=select_music_folder, font=("Arial",18))
button_select_folder.pack(pady=20)

#Create a listbox to display the songs
listb = tk.Listbox(window, width=50, font=("Arial", 12))
listb.pack(pady=20)


# Create a button to the previous song
button_previous= ctk.CTkButton(window, text="<", command= previous_song, width=50, font=("Arial", 18))
button_previous.pack(side=tk.LEFT, padx=5)

button_play= ctk.CTkButton(window, text="Play", command= play_song, width=50, font=("Arial", 18))
button_play.pack(side=tk.LEFT, padx=5)

button_pause= ctk.CTkButton(window, text="Pause", command= pause_song, width=50, font=("Arial", 18))
button_pause.pack(side=tk.LEFT, padx=5)

# Create a button to the next song
button_next= ctk.CTkButton(window, text=">", command= next_song, width=50, font=("Arial", 18))
button_next.pack(side=tk.LEFT, padx=5)