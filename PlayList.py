import csv
from Track import Track

class PlayList:
    
    def __init__(self, size: int = 0):
        
        self.storage0 = [None] * size
        self.size = 0

    def increaseSize(self):
        self.size +=1

    def getSize(self):
        return self.size

    def addtoPlaylist(self,song:Track):
        self.storage0=song

    def getByArtist(self, artist):
        """Returns a list of songs based on Artist name, else return none"""
        s=[]
        with open('Library.csv', 'r') as storage:
            read=csv.reader(storage)
            for lines in read:
                if artist in lines[1]:
                    t=Track(lines[0],lines[1],lines[2],lines[3])
                    s.append(t)
                else:
                    print("")
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
        total_seconds = 0

        for items in list:
            if items is None:
                break
            minutes, seconds = map(int, items.duration.split(":"))
            total_seconds += minutes * 60 + seconds

        total_minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        return f"{total_minutes}:{remaining_seconds:02d}"


    def __str__(self):
        plist="<-----PlayList----->\n"
        for i in self.storage0:
            plist+=f"{i}\n"
        plist+=f"\nTotal Duration: {self.getTotalDuration(self.storage0)}\n<-----End----->"
        return plist

            
        

pl=PlayList()

pl.addtoPlaylist(pl.getByArtist("Ariana Grande"))
print(pl)
# print(pl.getByArtist("Ariana Grande"))
# print(pl.getTotalDuration(pl.getByArtist("Ariana Grande")))
