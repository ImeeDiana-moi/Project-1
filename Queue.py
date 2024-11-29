import csv
import random
from Track import Track
# from PlayList import PlayList

class Queue:
    def __init__(self,size:int=50):
        """Create a Queue"""
        self.queue=[None]*size
        self.size=0
        self.curr = 0
        self.repeat = False
        self.shuffle= False
        self.state=True

    def increaseSize(self):
        """Increase Queue Size"""
        self.size +=1

    def setstate(self,mode):
        if mode == 1:
            self.state=False
        elif mode==2:
            self.state=True

    def getSize(self):
        """Return Queue Size"""
        return self.size

    def enqueue(self,song:Track):
        """Add song to Queue"""
        index=self.size
        self.queue[index]=song
        self.increaseSize()
    
    def listEnqueue(self, receive): 
        """Add a list of Track objects to the queue."""
        for track in receive:
            self.enqueue(track)

    def dequeue(self):
        """Remove Song from Queue"""
        if self.size==0:
            return None
        else:
            item=self.queue[0]
            self.queue=self.queue[1:]
            self.size-=1
            return item
        
    def getContent(self):
        str=f""
        index=0
        while index < len(self.queue):
            if self.queue[index]==None:
                break
            str+=f"[{self.queue[index]}]\n"
            index+=1
        return str
    
    def convert(self):
        """Convert content into list for storing data into csv file"""
        s=[]
        for items in self.queue:
            if items == None:
                break
            s += [[items]]
        return s
    
    def getTotalDuration(self):
        """Returns total duration of the playlist"""
        total=0
        for tracks in self.queue:
            total += int(tracks.duration)
        
        mins=total // 60
        seconds=total % 60
        
        return f"{mins}:{seconds:02d}"

    def skipTrack(self):
        if self.curr != -1 and self.curr < self.size - 1:
            self.curr += 1
            self.playTrack()
        else:
            if self.repeat:
                self.curr = 0
                self.playTrack()
            else:
                print("No more tracks left.")
                self.curr = -1
                return None
            
    def toggleRepeat(self):
        self.repeat = True

    def pauseTrack(self):
        self.state = False
    
    def playTrack(self):
        if self.curr == -1:
            self.curr = 0
        if self.curr < self.size and self.queue[self.curr] is not None:
            return(f"Currently Playing {'(Paused)' if self.state == False else ''}: \n\t{self.queue[self.curr]}\nNext track: \n\t{'No more tracks left' if self.queue[self.curr+1]==None else self.queue[self.curr+1]}")

    def prevTrack(self):
        self.state = True
        if self.curr > 0:
            self.curr -= 1
            self.playTrack()
        else:
            if self.repeat:
                self.curr = self.size - 1
                self.playTrack()
            else:
                self.playTrack()
                self.curr = -1
    
    def showQueue(self):
        if self.size==0:
            print("The queue is empty.")
        else:
            print("<------Songs in Queue------>")
            for i in range(self.size):
                print(f"\n{self.queue[i]}\n")
            print("<---------End of Queue--------->")
            
    def shuffleQueue(self):
        self.shuffle = True
        tracks = self.queue[:self.size]
        random.shuffle(tracks)
        self.queue[:self.size] = tracks

    def display(self):
        print(f"Total Duration: {self.getTotalDuration()}\nShuffled: {'YES' if self.shuffle == True else 'NO'}\tRepeat: {'NO' if self.repeat == False else 'YES'}")
        print(f"{self.playTrack()}")

    def clearQueue(self):
        self.queue = []


def loadTracksToQueue(queue):
    with open('Library.csv', mode='r') as storage:
        reader = csv.reader(storage)
        for line in reader:
            if len(line) >= 4:  # Ensure all required data is present
                title, artist, album, duration = line
                track = Track(title, artist, album, duration)
                queue.enqueue(track)
    print(f"Tracks loaded into the queue from Library.csv.\n")
    

# p=PlayList()
# # print(p.loadplaylist('my playlist'))

# # p.addtoPlaylist(p.loadplaylist('my playlist'))
# queue = Queue()
# queue.listEnqueue(p.convert()) 

# print(queue)
# queue.playTrack()
# queue.setstate(1)
# print(queue.player())

#wala ni apil tanan diri
# song1 = Track("Nikes", "Frank Ocean", "Blonde", "5:14")
# song2 = Track("Heartless", "The Weeknd", "After Hours", "3:18")
# song3 = Track("Thinkin Bout You", "Frank Ocean", "Channel Orange", "3:21")
# queue.enqueue(song1)
# queue.enqueue(song2)
# queue.enqueue(song3)
# # queue.repeat = True
# # queue.shuffle = True
# queue.pauseTrack()
# queue.display()

# print(queue.getTotalDuration())

# queue.toggleRepeat()

# queue.playTrack() #Play 1st song

# queue.skipTrack() #Skip to 2nd song
# # queue.playTrack() #PLay 2nd song

# queue.skipTrack() #Skip to 3rd song
# queue.prevTrack()
# queue.prevTrack()
# queue.skipTrack()
# queue.skipTrack()
# queue.playTrack() #Play 3rd song

# queue.prevTrack() #Go back to 2nd song
# queue.playTrack() #Play 2nd song

# queue.prevTrack() #Go back to 1st song
# queue.playTrack() #Play 1st song

# queue.prevTrack() #Go back to the last song in the queue
# queue.playTrack() #Play last song