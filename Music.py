import csv
import random
from datetime import datetime

class Music:
    """Receives information of a song, manage information"""
    
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration 
        
    def __str__(self):
        return f"{self.title} by {self.artist} (Album: {self.album})"
    
    
class PlayList:
    
    def __init__(self, size: int = 100):
        """Initialize playlist with a max size"""
        self.storage0 = [None] * size
        self.size = 0

    def increaseSize(self):
        # Increase the size of the playlist if needed
        if self.size >= len(self.storage0):
            self.storage0.extend([None] * len(self.storage0))
        self.size += 1

    def getSize(self):
        """Returns the current size of the playlist"""
        return self.size
    
    def addtoPlaylist(self, song: Music):
        """Add a Music object to the playlist"""
        if self.size < len(self.storage0):
            self.storage0[self.size] = song
        else:
            self.increaseSize()
            self.storage0[self.size - 1] = song
        self.size += 1
