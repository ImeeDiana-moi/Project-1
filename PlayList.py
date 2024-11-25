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

    # def getByArtist(self, artist):
    #     """Returns a list of songs based on Artist name, else return none"""
        
    def getBy(self, value, mode):
        """Get playlist based on value(either by title, artist, or album), 
        Mode: tr- individual track, ar- by artist, al by album"""
        with open('Library.csv', 'r') as storage:
                read=csv.reader(storage)
                if mode == "tr":
                    s=[]
                    for lines in read:
                        if value in lines[0]:
                            t=lines[[0],lines[1],lines[2],lines[3]]
                            s+=[t]
                    return s
                elif mode == "ar":
                    s=[]
                    for lines in read:
                        if value in lines[1]:
                            t=[lines[0],lines[1],lines[2],lines[3]]
                            s+=[t]
                    return s
                elif mode == "al":
                    s=[]
                    
                    for lines in read:
                        if value in lines[2]:
                            t=lines[0],lines[1],lines[2],lines[3]
                            s+=[t]
                    return s
                return "Nothing"
    
    
    def addtoStorage(self, name): #Need improvement
        """Adds the Playlist into the csv file
        Arguments: Name(Set a custom name for the queue)"""
        data=[]
        for items in self.convert():
            data+=[[name,items[0],items[1],items[2],items[3]]]
        # return data
        manage=open('Playlists.csv', 'a',newline='')
        write= csv.writer(manage)
        write.writerows(data)
        manage.close()

    # def getByAlbum(self, album):
    #     """Returns a list of songs based on Artist name, else return none"""
    #     album=str(album)
    #     s=[]
    #     with open('Library.csv', 'r') as storage:
    #         read=csv.reader(storage)
    #         for lines in read:
    #             if album in lines[2]:
    #                 t=Track(lines[0],lines[1],lines[2],lines[3])
    #                 s+=[t]
    #     return s
    
    def arrangeAlphabetically(self, playlist): #Bonuss
        """Arranges the received Playlist Alphabetically
        List: list from getBy() methods
        Returns alphabeticalized List of Songs but still follows the format"""
        
        pass

    def findcustomplaylist(self, name): #need improvement
        with open("Storage.csv", mode='r',newline='') as reader:
            read=csv.reader(reader)
            plays=f"<-----{name}----->"
            for i in read:
                if name in i[0]:
                    plays+=f""
                print("Wakay Pulos")
    
    def shuffle(self): #Bonus
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
    
    def convert(self):
        """Convert content into list for storing data into csv file"""
        s=[]
        for items in self.storage0:
            if items == None:
                break
            s +=[[items[0],items[1],items[2],items[3]]]
        return s


    def __str__(self):
        plist="Playlist\n"
        for items in self.storage0:
            plist+=f"\nTitle: {items[0]}\nArtist: {items[1]}\nAlbum: {items[2]}\nDuration: {items[3]}\n"
        return plist

        # if self.getSize() == 0:
        #     return "Playlist is Empty!"
        # plist=f"Playlist Name: {self.getpName()}"
        
        
    

            
        

pl=PlayList()
# pl.addtoPlaylist(pl.getBy("Ariana Grande","ar"))
# print(pl)
# print(pl.getBy("Ariana Grande",'ar'))
# pl.addtoPlaylist(pl.getBy("Ariana Grande",'ar'))
# # print(pl.convert())
# # print(pl.addtoStorage("Custom"))
# pl.addtoStorage("FUck Yeah")
# # pl.findcustomplaylist("Custom")
# print(pl.addtoPlaylist(pl.getByAlbum("1989")))
# print(pl)
# print(pl.getTotalDuration(pl.getByArtist("Ariana Grande")))
