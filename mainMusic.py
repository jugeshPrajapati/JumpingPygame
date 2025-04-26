import os, sys
# Ensure Python can import your sibling .py files
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mainSetting import *
import pygame
pygame.init()
pygame.mixer.init()


MUSIC_ENDED = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_ENDED)
pygame.display.set_mode((width,height))
songs=[]
song_index=0

# Define base directory and sound path relative to this file
BASE_DIR = os.path.dirname(__file__)
SOUND_PATH = os.path.join(BASE_DIR, MUSIC_PATH)
def load_music(path):
    
    global songs
    for filename in os.listdir(path):
        if filename.endswith('.xoht'):
            songs.append(os.path.join(path, filename))
    return songs


def runP():
    pygame.mixer.init()
    # load_music should accept a directory path
    songs = load_music(path=SOUND_PATH)

    global song_index  # The current song to load
    pygame.mixer.music.load(songs[song_index])
    pygame.mixer.music.play()
    song_index += 1
def whi(event):
          
    if event.type == MUSIC_ENDED:
        global song_index,songs
        song_index = (song_index + 1) % len(songs)  # Go to the next song (or first if at last).
        pygame.mixer.music.load(songs[song_index])
        pygame.mixer.music.play()
        
    pygame.display.update()
def bgmusic():
    pygame.mixer.music.load(os.path.join(SOUND_PATH, 'music.mp3'))
    pygame.mixer.music.play()

# Play an alternate background music track
def bgmus():
    pygame.mixer.music.load(os.path.join(SOUND_PATH, 'coolbeansbgmusic.mp3'))
    pygame.mixer.music.play()




