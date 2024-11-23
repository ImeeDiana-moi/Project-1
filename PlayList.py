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

    # def addtoPlaylist(self,song:Track):
    #     self.storage0=song
    def addtoPlaylist(self,list):
        for items in list:
            self.storage0+=[items]

    def getByArtist(self, artist):
        """Returns a list of songs based on Artist name, else return none"""
        
        with open('Library.csv', 'r') as storage:
            read=csv.reader(storage)
            s=[]
            for lines in read:
                if artist in lines[1]:
                    t=Track(lines[0],lines[1],lines[2],lines[3])
                    s+=[t]
        return s
    
    def getByAlbum(self, album):
        """Returns a list of songs based on Artist name, else return none"""
        album=str(album)
        s=[]
        with open('Library.csv', 'r') as storage:
            read=csv.reader(storage)
            for lines in read:
                if album in lines[2]:
                    t=Track(lines[0],lines[1],lines[2],lines[3])
                    s+=[t]
        return s
    
    def arrangeAlphabetically(self, playlist):
        """Arranges the received Playlist Alphabetically
        List: list from getBy() methods
        Returns alphabeticalized List of Songs but still follows the format"""\
        
        pass

    def convert(self):
        """Convert content into list for storing data into csv file"""
        s=[]
        for items in self.storage0:
            if items == None:
                break
            s +=items
        return s

    def addtoStorage(self, name):
        """Adds the queue into the csv file
        Arguments: Name(Set a custom name for the queue)"""
        data=[[name,self.convert()]]
        manage=open('Storage.csv', 'a',newline='')
        write= csv.writer(manage)
        write.writerows(data)
        manage.close()

    def findcustomplaylist(self, name):
        with open("Storage.csv", mode='r',newline='') as reader:
            read=csv.reader(reader)
            for i in read:
                if name in i[0]:
                    for items in i[1]:
                        print(items)
                print("Wakay Pulos")
    
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

    def getTotalDuration(self, list):
        """Returns total duration of the playlist"""
    
        TotalDuration = 0
        for track in self.storage0:
            if track is None:
                continue 
            duration = track.duration  
            minutes, seconds = duration.split(":")  
            TotalDuration += int(minutes) * 60 + int(seconds)  
        
        Total_Minutes = TotalDuration // 60
        total_Seconds = TotalDuration % 60
        result = f"Total Time: {Total_Minutes}:{total_Seconds} \nTotal Time(s): {TotalDuration}s"
        return result

    def __str__(self):
        plist="<-----PlayList----->\n"
        for i in self.storage0:
            plist+=f"\n{i}\n"
        plist+=f"Total Duration \n{self.getTotalDuration(self.storage0)}\n<-----End----->"
        return plist

            
        

pl=PlayList()

pl.addtoPlaylist(pl.getByArtist("Ariana Grande"))
# pl.addtoStorage("Custom")
# pl.findcustomplaylist("Custom")
# print(pl.addtoPlaylist(pl.getByAlbum("1989")))
print(pl)
# print(pl.getTotalDuration(pl.getByArtist("Ariana Grande")))
