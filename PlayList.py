import csv
from Track import Track
import LibraryManager
from Queue import Queue


playlists=[]
def loadplaylist():
    with open('Playlists.csv',mode='r',newline='') as playlist:
        read=csv.reader(playlist)
        for items in read:
            playlists.append(Track(items[0],items[1],items[2],items[3],items[4]))
#Do not delete this code



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
        """Return name of current playlist"""
        for items in self.storage0:
            return items.playlist

    def getPlaylist(self,playlist_name):
        """Gets tracks of playlist and add to self.storage"""
        for items in playlists:
            if items.playlist == playlist_name:
                self.storage0.append(items)
            self.increaseSize()

    def showTracksInPlaylist(self,playlist_name):
        """
        Displays tracks in the current playlist.
        """
        if not self.storage0:
            return "No tracks in the selected playlist."
        count = 1
        for items in playlists:
            if items.playlist == playlist_name:
                print(f"[{count}]{str(items)}\n")
                count += 1

    def sendtoQueue(self,playlist_name):
        s=[]
        for items in playlists:
            if items.playlist==None:
                break
            if items.playlist == playlist_name:
             s.append(items)
        return s
    
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
            total += int(tracks.duration)
        
        mins=total // 60
        seconds=total % 60
        
        return f"{mins}:{seconds:02d}"
            
     

    def __str__(self):
        """Returns Details of the current playlist"""
        if self.getSize()==0:
            return 'No playlist selected'
        s=f"Playlist Name: {self.getPlaylistName()}\nTotal Duration: {self.getTotalDuration()}\nTracks:\n"
        for i in self.storage0:
            s+=f'\t{i}\n'
        return s
    
def show():
    e=open('Playlists.csv', 'a',newline='')
    w=csv.writer(e)
    count=1
    for tracks in LibraryManager.Library:
        print(f"({count}) {tracks.title}")
        count+=1
    return w
        
def createplaylist(name):
    """Receives a name to create a playlist and choose tracks from library only"""
    w=show()
    while True:
        try:
            ind=int(input("Choose Tracks(0 to exit): "))
        except:
            print("Enter valid Choice.")
        
        if ind == 0:
            break
        elif ind > len(LibraryManager.Library):
            print("Index out of range.")
            continue
        track=LibraryManager.Library[ind-1]
        w.writerows([[track.title,track.artist,track.album,track.duration,name]])
        print("Track added!")
    
def showplaylists():
    """Prints Playlist names from Playlist csv>
    Return None if playlist.csv is empty"""
    print("<-----Playlists----->")
    if len(playlists)==0:
        print("No Playlists. Create one.\n")
        return None
    count=1
    l=[]
    for items in playlists:
        if items.playlist not in l:
            l.append(items.playlist)
    for items in l:
        print(f"({count}) {items}")
        count+=1
    return l

loadplaylist()




#Tests

# createplaylist("My Playlist")
# showplaylists()
# pl=PlayList()
# # print(pl)
# pl.getPlaylist("Imee")
# print(pl.sendtoQueue())
# q=Queue()
# q.listEnqueue(pl.sendtoQueue())
# print(q.display())
# print(pl.getTotalDuration())
                

