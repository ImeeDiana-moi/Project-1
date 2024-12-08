from Track import Track
import LibraryManager
from Queue import Queue
# LibraryManager.loadLibrary()
class PlayList:
    
    def __init__(self, size: int = 0):
        
        self.storage0 = [None] * size
        self.size = 0

    def increaseSize(self):
        self.size +=1

    def getSize(self):
        return self.size


    def getPlaylistName(self):
        """Return name of current playlist"""
        for items in self.storage0:
            return items.playlist

    def showPlaylistAlpha(self):
        """Shows the Playist(Default: Alphabetical)"""
        if not self.storage0 or all(track is None for track in self.storage0):
            print("The playlist is empty or invalid.")
            return
        def get_track_title(track):
            return track.gettitle().lower()
        
        self.storage0 = sorted(self.storage0, key=get_track_title)


    def getPlaylist(self,playlist_name):
        """Gets tracks of playlist and add to self.storage"""
        for items in LibraryManager.Library:
            if items.getPlaylist() == playlist_name:
                if items not in self.storage0:
                    self.storage0.append(items)
                    self.increaseSize()

    def showTracksInPlaylist(self):
        """
        Displays tracks in the current playlist.
        """
        if not self.storage0:
            return "No tracks in the selected playlist."
        for tracks in self.storage0:
            print(f"{tracks}")
        # for items in LibraryManager.Library:
        #     if items.playlist == playlist_name:
        #         print(f"[{count}]{str(items)}")
        #         count += 1

    def sendtoQueue(self,playlist_name):
        s=[]
        for items in LibraryManager.Library:
            if items.playlist==None:
                break
            if items.playlist == playlist_name:
             s.append(items)
        return s
    
    def shuffle(self): #Bonus
        """shuffle playlist"""
        import random
        if not self.storage0 or all(track is None for track in self.storage0):
            print("The playlist is empty.")
        random.shuffle(self.storage0)    

    def shuffle_list(self):
    # Make a copy to avoid modifying the original list
        shuffled = self.storage0[:]
        n = len(shuffled)
        
        for i in range(n - 1, 0, -1):
            random_index = (i * 123456789) % (i + 1)
            shuffled[i], shuffled[random_index] = shuffled[random_index], shuffled[i]
        
        self.storage0=shuffled

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
            
    def str(self):
        """Returns Details of the current playlist
        Should be in pagination format"""
        res= LibraryManager.paginate_items(self.storage0)
        return res
        # if self.getSize()==0:
        #     return 'No playlist selected'
        # s=f"Playlist Name: {self.getPlaylistName()}\nTotal Duration: {self.getTotalDuration()}\nTracks:\n"
        # for i in self.storage0:
        #     s+=f'\t{i}\n'
        # return s
    
# pl=PlayList()
# pl.getPlaylist("None")
# # print(pl.str())
# pl.showTracksInPlaylist()
# LibraryManager.showLibrary()






#Tests

# createplaylist("My Playlist")
# showplaylists()
# pl=PlayList()
# # # print(pl)
# pl.getPlaylist("My Playlist")
# pl.showPlaylistAlpha()
# print(pl)
# print(pl.sendtoQueue())
# q=Queue()
# q.listEnqueue(pl.sendtoQueue())
# print(q.display())
# print(pl.getTotalDuration())
                


# test shuffle

# playlist = PlayList(size=0)

# track1 = Track("Juno", "Sabrina Carpenter", "Album1", 180)
# track2 = Track("Good Graces", "Sabrina Carpenter", "Album2", 250)
# track3 = Track("Bed Chem", "Sabrina Carpenter", "Album3", 190)
# track4 = Track("Because I Liked a Boy", "Sabrina Carpenter", "Album4", 300)

# playlist.storage0 = [track1, track2, track3, track4]

# # print("Original Order:")
# # for i, track in enumerate(playlist.storage0, start=1):
# #     print(f"[{i}] {track}")

# playlist.shuffle()

# # print("\nShuffled Order:")
# # for i, track in enumerate(playlist.storage0, start=1):
# #     print(f"[{i}] {track}")

# print (playlist)

# test showPlaylistAlpha

# playlist = PlayList(size=0)
# track1 = Track("SZA", "artist1", "album1", 280)
# track2 = Track("Frank Ocean", "artist2", "album2", 600)
# track3 = Track("Lady Gaga", "artist3", "album3", 120)

# playlist.storage0 = [track1, track2, track3]

# playlist.showPlaylistAlpha()