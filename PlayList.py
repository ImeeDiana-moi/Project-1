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
            self.increaseSize()


    def getPlaylistName(self):
        for items in self.storage0:
            if items[0]!=None:
                return items[0]
            return None
        
    def loadplaylist(self,playlistname):
        with open('Playlists.csv',mode='r',newline='') as playlist:
            read=csv.reader(playlist)
            for items in read:
                if items[0]==playlistname:
                    self.storage0+=Track(items[0],items[1],items[2],items[3],items[4])

        
    # def getBy(self, value, mode):
    #     """Get playlist based on value(either by title, artist, or album), 
    #     Mode: tr- individual track, ar- by artist, al by album"""
    #     with open('Library.csv', 'r') as storage:
    #             read=csv.reader(storage)
    #             if mode == "tr":
    #                 s=[]
    #                 for lines in read:
    #                     if value in lines[0]:
    #                         t=[lines[[0],lines[1],lines[2],lines[3]]]
    #                         s+=[t]
    #                 return s
    #             elif mode == "ar":
    #                 s=[]
    #                 for lines in read:
    #                     if value in lines[1]:
    #                         t=[lines[0],lines[1],lines[2],lines[3]]
    #                         s+=[t]
    #                 return s
    #             elif mode == "al":
    #                 s=[]
                    
    #                 for lines in read:
    #                     if value in lines[2]:
    #                         t=[lines[0],lines[1],lines[2],lines[3]]
    #                         s+=[t]
    #                 return s
    #             return "Nothing"
    
    
    # def addtoStorage(self, name):
    #     """Adds the Playlist into the csv file
    #     Arguments: Name(Set a custom name for the queue)"""
    #     data=[]
    #     for items in self.convert():
    #         data+=[[name,items[0],items[1],items[2],items[3]]]

    #     manage=open('Playlists.csv', 'a',newline='')
    #     write= csv.writer(manage)
    #     write.writerows(data)
    #     manage.close()
    
    # def arrangeAlphabetically(self, playlist): #Bonuss
    #     """Arranges the received Playlist Alphabetically
    #     List: list from getBy() methods
    #     Returns alphabeticalized List of Songs but still follows the format"""
        
    #     Arranged = [track for track in self.storage0 if track is not None]
    #     word = len(Arranged)

    #     for i in range(word):
    #         for j in range (0, word - i - 1):
    #             if Arranged[j][0] > Arranged[j+1][0]:
    #                 Arranged[j], Arranged[j+1] = Arranged[j+1], Arranged[j]
    #     return f"Sorted Playlist \n{Arranged}"
 
    # def findcustomplaylist(self, name): #need improvement
    #     with open("Playlists.csv", mode='r',newline='') as reader:
    #         read=csv.reader(reader)
    #         plays=f"<-----{name}----->"
    #         for items in read:
    #             if items[0]==name:
    #                 plays+=f"\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}"
                
    #         return plays
    
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

    def getTotalDuration(self):
        """Returns total duration of the playlist"""
        total=0
        for tracks in self.storage0:
            total + tracks.duration
        
        mins=total//60
        seconds=total % 60
        
        return str(mins)+":"+str(seconds)
            
        # TotalDuration = 0
        # for track in self.storage0:
        #     if track is None:
        #         continue 
        #     duration = track[4]
        #     minutes, seconds = duration.split(":")  
        #     TotalDuration += int(minutes) * 60 + int(seconds)  
        
        # Total_Minutes = TotalDuration // 60
        # total_Seconds = TotalDuration % 60
        # result = f"{Total_Minutes}mins {total_Seconds:02d}s"
        # return result
    
    # def convert(self):
    #     """Convert content into list"""
    #     s=[]
    #     for items in self.storage0:
    #         if items == None:
    #             break
    #         s +=[[items[0],items[1],items[2],items[3],items[4]]]
    #     return s
    
    
    # def showplaylists(self,name, mode):
    #     """Shows playlist (specific or all)
    #     Mode: 'all'-show all playlists, 'cus'-show specific playlist"""
    #     with open('Playlists.csv',mode='r',newline='') as playlist:
    #         read=csv.reader(playlist)
    #         songs=f'<-----{name}----->\n'
    #         if mode == 'all':
    #             for items in read:
    #                 songs+=f'\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}\n'
    #         elif mode == 'cus':
    #             for items in read:
    #                 if items[0]==name:
    #                     songs+=f'\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}\n'

    #         songs+='<----End----->'
    #         print (songs)

    # def listplaylists(self):
    #     with open('Playlists.csv',mode='r',newline='') as playlist:
    #         read=csv.reader(playlist)
    #         all=[]
    #         iter=1
    #         for lists in read:
    #             if lists[0] not in all:
    #                 all+=[lists[0]]
    #         plays=f"<-----Playlists----->\n"  
    #         for items in all:
    #             plays+=f"[{iter}] {items}\n" 
    #             iter+=1  

    #         plays+="<-----End----->"   
    #         print(plays)
    #         return all
            
    # def addPlaylist(self,name):
    #     with open("Library.csv",mode='r',newline='') as reader:
    #         read=csv.reader(reader)
    #         library=[]
    #         counter=1
    #         for items in read:
    #             library+=[items]
    #             print(f"[{counter}] {items[0]}")
    #             counter+=1
    #         while True:
    #             try:
    #                 index=int(input("Enter Track Number(0 to Finish): "))
    #             except ValueError:
    #                 print("Invalid Input. Please Enter a number.")
    #                 continue
    #             if index ==0:
    #                 break
    #             elif index >= len(library):
    #                 print("Invalid! Choose again!")
    #                 continue
    #             pl=open('Playlists.csv',mode='r',newline='')
    #             reada=csv.reader(pl)

    #             data=[[name]+library[index-1]]
                
    #             manage=open('Playlists.csv', 'a',newline='')
    #             write= csv.writer(manage)
    #             write.writerows(data)
    #             manage.close()

    def __str__(self):
        if self.getSize()==0:
            return 'Select Playlist'
        s=f"Playlist Name: {self.getPlaylistName()}\nTotal Duration: {self.getTotalDuration()}\nTracks:\n"
        # for i in self.storage0:
        #     print(i)
        return s
            
        
pl=PlayList()
print(pl)
                


    # def playlistbypage(self):
    #     page=1
    #     if self.getSize()!=0:
    #         plist=f'Playlist Name: {self.getPlaylistName()}\nTotal Duration: {self.getTotalDuration(self.storage0)}\nTracks:\n'
    #         counter=1
    #         maxpage=1
    #         for songs in self.storage0:
    #             plist+=f'[{counter}] {songs[1]}\n'
    #             counter+=1
    #         if counter > 6:
    #             maxpage+=1
    #         plist+=f"Page {page} of {maxpage}"
    #         return plist
    #     else:
    #         return "Nothing In playlist"
    # def playlistbypage(self, page=1, items_per_page=5):
    #     """
    #     Displays the list of playlists with pagination.

    #     Args:
    #         playlists (list[str]): List of playlist names.
    #         page (int): Current page number.
    #         items_per_page (int): Number of playlists to display per page.
    #     """
    #     playlists=self.storage0
    #     total_playlists = len(playlists)
    #     total_pages = (total_playlists + items_per_page - 1) // items_per_page  # Ceiling division

    #     # Validate and adjust the current page
    #     page = max(1, min(page, total_pages))

    #     # Calculate the range of playlists to display
    #     start_index = (page - 1) * items_per_page
    #     end_index = min(start_index + items_per_page, total_playlists)
    #     playlists_to_display = playlists[start_index:end_index]

    #     print("\n<----- Playlists ----->")
    #     for idx, playlist in enumerate(playlists_to_display, start=start_index + 1):
    #         print(f"[{idx}] {playlist}")

    #     print(f"\n<Page {page} of {total_pages}>\n[11] Previous Page\n[12] Next Page\n[0] Exit to Main Menu")

    #     return page


# pl=open('Playlists.csv',mode='r',newline='')
# read=csv.reader(pl)
# for i in read:
#     print(i)
# pl=PlayList()
# # print(pl.playlistbypage())
# prinat=pl.loadplaylist("my playlist")
# pl.addtoPlaylist(prinat)
# pl.addtoPlaylist(prinat)
# pl.addtoPlaylist(prinat)
# # # print(pl.getPlaylistName())
# pl.playlistbypage()
# pl.playlistbypage(2)
# pl.playlistbypage(3)
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

# pl.addtoPlaylist([
#     ["Ahank U Next", "Ariana Grande", "Thank U Next", "3:27"],
#     ["CRings, Ariana Grande", "Thank U Next", "2:58"],
#     ["Break Free", "Ariana Grande", "My Everything, 3:34"]
# ])

# print(pl.arrangeAlphabetically(pl.storage0))