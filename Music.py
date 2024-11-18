import csv
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
    
    def getTitle(self):
        return self.title
    
    def getDuration(self):
        return self.duration
    
    def convertTime(self):
        time=self.duration
        minutes, seconds = map(int, time.split(":"))
        total_seconds = minutes * 60 + seconds
        return total_seconds
        
    def getSongDetails(self, title):
        """Returns the details of the song in the format
        Title:
        Artis:
        Album:
        Duration:
        Arguments: Title of the song"""
        artist=title
        with open('Library.csv', 'r') as storage:
            read=csv.reader(storage)
            for lines in read:
                # print(lines[1])
                if artist in lines[0]:
                    return(f"Title: {lines[0]}\nArtist: {lines[1]}\nAlbum: {lines[2]}\nDuration: {lines[3]}")
                else:
                    return "Song does not Exist"
    
    def __str__(self):
        return f"Title: {self.getTitle()}\nArtist: {self.getArtist()}\nAlbum: {self.getAlbum()}\nDuration: {self.getDuration()}"
    

