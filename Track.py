import csv
from datetime import datetime

class Track:
    """Receives information of a song, manage information"""
    
    def __init__(self, title, artist, album, duration,playlist=None):
        """Receive duration as seconds"""
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.playlist=playlist
    
    def gettitle(self):
        return self.title
    def getartist(self):
        return self.artist
    def getalbum(self):
        return self.album
    def getduration(self):
        # 208 seconds
        minutes = int(self.duration) // 60
        seconds = int(self.duration) % 60
        return str(minutes) + ":" + str(seconds)
    
    def settitle(self, newtitle):
        self.title=newtitle
    def setartist(self, newartist):
        self.artist=newartist
    def setalbum(self, newalbum):
        self.album=newalbum
    def setduration(self, newduration):
        self.duration=newduration

    def converToCSV(self):
        pass

    def details(self):
        return f"Title: {self.title}\nArtist: {self.artist}\nAlbum: {self.album}\nDuration: {self.duration}"
    
    def __str__(self):
        if self.playlist=="None":
            self.playlist='Unknown Playlist'
        return f'{self.title}-{self.artist}({self.getduration()})-{self.playlist}'
    
def addTrack():
    pass