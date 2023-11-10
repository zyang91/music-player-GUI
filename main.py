import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
import os
import pygame
import time
from mutagen.mp3 import MP3

#Initilize pygame
pygame.mixer.init()

#Store the song playing position
current =0
paused = False
selected_folder_path = ""

def select_music_folder():
    global selected_folder_path
    selected_folder_path = filedialog.askdirectory()
    if selected_folder_path:
        listb.delete(0, tk.END)
        for file in os.listdir(selected_folder_path):
            if file.endswith(".mp3"):
                listb.insert(tk.END, file)

def previous_song():
    if len (listb.curselection()) > 0:
        current_index = listb.curselection()[0]
        if current_index > 0:
            listb.selection_clear(0, tk.END)
            listb.selection_set(current_index - 1)
            play_selected_song()

def next_song():
    if len (listb.curselection()) > 0:
        current_index = listb.curselection()[0]
        if current_index < listb.size() - 1:
            listb.selection_clear(0, tk.END)
            listb.selection_set(current_index + 1)
            play_selected_song()

def play_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        play_selected_song()

def play_selected_song():
    global current_position, paused
    if len (listb.curselection()) > 0:
        current_index = listb.curselection()[0]
        selected_song = listb.get(current_index)
        full_path =os.path.join(selected_folder_path, selected_song)
        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play(start=current_position)
        paused = False
        audio = MP3(full_path)
        song_length = audio.info.length
        prog_bar['maximum'] = int(song_length)

    
def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True

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

#Create  a frame to control buttons
frame = tk.Frame(window)
frame.pack(pady=20)

# Create a button to the previous song
button_previous= ctk.CTkButton(frame, text="<", command= previous_song, width=50, font=("Arial", 18))
button_previous.pack(side=tk.LEFT, padx=5)

button_play= ctk.CTkButton(frame, text="Play", command= play_song, width=50, font=("Arial", 18))
button_play.pack(side=tk.LEFT, padx=5)

button_pause= ctk.CTkButton(frame, text="Pause", command= pause_song, width=50, font=("Arial", 18))
button_pause.pack(side=tk.LEFT, padx=5)

# Create a button to the next song
button_next= ctk.CTkButton(frame, text=">", command= next_song, width=50, font=("Arial", 18))
button_next.pack(side=tk.LEFT, padx=5)


#progress bar
prog_bar= Progressbar(window, orient=tk.HORIZONTAL, length=400, mode='determinate')
prog_bar.pack(pady=10)

window.mainloop()