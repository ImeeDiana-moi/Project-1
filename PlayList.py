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

    def addtoPlaylist(self,list):

        for items in list:
            self.storage0+=[items]
        
    def getBy(self, value, mode):
        """Get playlist based on value(either by title, artist, or album), 
        Mode: tr- individual track, ar- by artist, al by album"""
        with open('Library.csv', 'r') as storage:
                read=csv.reader(storage)
                if mode == "tr":
                    s=[]
                    for lines in read:
                        if value in lines[0]:
                            t=[lines[[0],lines[1],lines[2],lines[3]]]
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
                            t=[lines[0],lines[1],lines[2],lines[3]]
                            s+=[t]
                    return s
                return "Nothing"
    
    
    def addtoStorage(self, name):
        """Adds the Playlist into the csv file
        Arguments: Name(Set a custom name for the queue)"""
        data=[]
        for items in self.convert():
            data+=[[name,items[0],items[1],items[2],items[3]]]

        manage=open('Playlists.csv', 'a',newline='')
        write= csv.writer(manage)
        write.writerows(data)
        manage.close()
    
    def arrangeAlphabetically(self, playlist): #Bonuss
        """Arranges the received Playlist Alphabetically
        List: list from getBy() methods
        Returns alphabeticalized List of Songs but still follows the format"""
        
        pass

    def findcustomplaylist(self, name): #need improvement
        with open("Playlists.csv", mode='r',newline='') as reader:
            read=csv.reader(reader)
            plays=f"<-----{name}----->"
            for items in read:
                if items[0]==name:
                    plays+=f"\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}"
                
            return plays
    
    def shuffle(self): #Bonus
        """Receives a list from getBy() methods and return the list in shuffled order"""
        pass    
    
    def showPlaylistAlpha(self):
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
            duration = track[3]
            minutes, seconds = duration.split(":")  
            TotalDuration += int(minutes) * 60 + int(seconds)  
        
        Total_Minutes = TotalDuration // 60
        total_Seconds = TotalDuration % 60
        result = f"Total Time: {Total_Minutes}:{total_Seconds:02d}\nTotal Time(s): {TotalDuration}s"
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
        plist+=f"\n{self.getTotalDuration([])}"
        return plist
    
def addPlaylist(name):
    with open("Library.csv",mode='r',newline='') as reader:
        read=csv.reader(reader)
        library=[]
        counter=1
        for items in read:
            library+=[items]
            print(f"[{counter}] {items[0]}")
            counter+=1
        while True:
            try:
                index=int(input("Enter Track Number(0 to Finish): "))
            except ValueError:
                print("Invalid Input. Please Enter a number.")
                continue
            if index ==0:
                break
            data=[[name]+library[index-1]]
            manage=open('Playlists.csv', 'a',newline='')
            write= csv.writer(manage)
            write.writerows(data)
            manage.close()

def showplaylists(name, mode):
    """Shows playlist (specific or all)
    Mode: 'all'-show all playlists, 'cus'-show specific playlist"""
    with open('Playlists.csv',mode='r',newline='') as playlist:
        read=csv.reader(playlist)
        songs=f'<-----{name}----->\n'
        if mode == 'all':
            for items in read:
                songs+=f'\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}\n'
        elif mode == 'cus':
            for items in read:
                if items[0]==name:
                    songs+=f'\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}\n'

        songs+='<----End----->'
        print (songs)
# showplaylists("me","all")

def listplaylists():
    with open('Playlists.csv',mode='r',newline='') as playlist:
        read=csv.reader(playlist)
        all=[]
        iter=1
        for lists in read:
            if lists[0] not in all:
                all+=[lists[0]]
        plays=f"<-----Playlists----->\n"  
        for items in all:
            plays+=f"[{iter}] {items}\n" 
            iter+=1  

        plays+="<-----End----->"   
        print(plays)
        return all
        
        
# listplaylists()         


        
        

            
        

# pl=PlayList()
# pl.addtoPlaylist(pl.getBy("Ariana Grande","ar"))
# # print(pl)
# # pl.addtoStorage("Imee")
# print(pl.findcustomplaylist("Imee"))
# # print(pl.getBy("Ariana Grande",'ar'))
# # pl.addtoPlaylist(pl.getBy("Ariana Grande",'ar'))
# # # print(pl.convert())
# # # print(pl.addtoStorage("Custom"))
# # pl.addtoStorage("FUck Yeah")
# pl.findcustomplaylist("Imee")
# print(pl.addtoPlaylist(pl.getByAlbum("1989")))
# print(pl)
# print(pl.getTotalDuration(pl.getByArtist("Ariana Grande")))
