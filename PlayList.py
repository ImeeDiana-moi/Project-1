import csv
from Music import Music

class PlayList:
    
    def __init__(self, size: int = 100):
        
        self.storage0 = [None] * size
        self.size = 0

    def increaseSize(self):
        self.size +=1

    def getSize(self):
        return self.size

    def addtoPlaylist(self,song:Music):
        index=self.size
        self.storage0[index]=song
        self.increaseSize()

    def getByArtist(self, artist):
        """Returns a list of songs based on Artist name, else return none"""
        s=[]
        with open('Library.csv', 'r') as storage:
            read=csv.reader(storage)
            # next(read) #skipping the track format guide
            for lines in read:
                if artist in lines[1]:
                    s+= [lines]
            
        return s
    
    def getByAlbum(self, album):
        """Returns a list of songs based on Artist name, else return none"""
        album=str(album)
        s=[]
        with open('Library.csv', 'r') as storage:
            read=csv.reader(storage)
            # next(read) #skipping the track format guide
            for lines in read:
                if album in lines[2]:
                    s+= [lines]
            
        return s
    
    def createPlaylist(self,list):
        """Receives List from getBy() methods and creates a Playlist"""
        artist=list[0][1]
        
        hd=f"<-----{artist}----->"
        for items in list:
            hd+=f"\n{items[0]}"
            # for details in items:
            #     hd+=f"\n{details}"

        return hd
    
    def arrangeAlphabetically(self,list):
        """Arranges the received Playlist Alphabetically
        List: list from getBy() methods
        Returns alphabeticalized List of Songs but still follows the format"""
        pass

    def shuffle(self):
        """Receives a list from getBy() methods and return the list in shuffled order"""
        pass
    
    def showPlaylist(self):
        """Shows the Playist(Default: Alphabetical)"""
        pass
    
    def convertTime(self):
        
        time=self.duration
        minutes, seconds = map(int, time.split(":"))
        total_seconds = minutes * 60 + seconds
        return total_seconds

    def getTotalDuration(self,list):
        """Returns total duration of the playlist"""
        """Complete this method"""
        pass


    def __str__(self):
        return self.storage0

