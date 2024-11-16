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
    

    def getDuration(self, Filepath = None):
        if Filepath:
            total = 0 
            with open (Filepath, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    duration = row[-1].strip()
                    minutes, seconds = map(int, duration.split(":"))
                    total_seconds += minutes * 60 + seconds

            minutes = total_seconds // 60
            seconds = total_seconds % 60
            return f"Total Song Duration: {minutes} : {seconds : 02}"
        
        else:
            minutes = self.duration // 60
            seconds = self.duration % 60
            return f"{minutes} : {seconds :02}"


    def getTitle(self):
        return self.title
    
    def getSongDetails(self, title):
        """Returns the details of the song in the format
        Title:
        Artis:
        Album:
        Duration:
        Arguments: Title of the song"""
        artist=title
        with open('Storage.csv', 'r') as storage:
            read=csv.reader(storage)
            for lines in read:
                # print(lines[1])
                if artist in lines[0]:
                    return(f"Title: {lines[0]}\nArtist: {lines[1]}\nAlbum: {lines[2]}\nDuration: {lines[3]}")
                else:
                    return "Song does not Exist"
    
    def __str__(self):
        return f"Title: {self.getTitle()}\nArtist: {self.getArtist()}\nAlbum: {self.getAlbum()}\nDuration: {self.getDuration()}"
    
# m0=Music("Rap God", "Eminem", "2:00","Niga")
# print(m1.getDuration())
# m1.convertduration()
# print(m1.getSongDetails("Break"))
# print(m0)