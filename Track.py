import csv
import random
from datetime import datetime

class Track:
    """Receives information of a song, manage information"""
    
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
    
    def gettitle(self):
        return self.title
    def getartist(self):
        return self.artist
    def getalbum(self):
        return self.album
    def getduration(self):
        return self.duration
    
    def settitle(self, newtitle):
        self.title=newtitle
    def setartist(self, newartist):
        self.artist=newartist
    def setalbum(self, newalbum):
        self.album=newalbum
    def setduration(self, newduration):
        self.duration=newduration
    
        
    def __str__(self):
        return f"Title: {self.title}\nArtist: {self.artist}\nAlbum: {self.album}\nDuration: {self.duration}"