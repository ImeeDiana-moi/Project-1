class Music:
    """Receives information of a song, manage information"""
    
    def __init__(self, title, artist, duration,album=None):
        self.title=title
        self.artist=artist
        self.album=album
        self.duration=duration

    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist
    def getAlbum(self):
        if self.album == None:
            return "Unknown"
        return self.album
    def getDuration(self):
        return self.duration
    def getTitle(self):
        return self.title
    
    def convertduration(self):
        s=self.getDuration()
        index=0
        time=0
        while index < len(s):
            print(s[index],end='')
            index+=1


    def __str__(self):
        return f"{self.title},{self.artist},{self.album},{self.duration}"
    
m1=Music("Rap God", "Eminem", "2:00","Nigga")
print(m1.getDuration())
m1.convertduration()