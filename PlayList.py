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
        
