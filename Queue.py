import csv
from Music import Music

class Queue:
    """Creates a Queue"""
    
    def __init__(self,size:int=50):
        self.queue=[None]*size
        self.size=0

    def increaseSize(self):
        self.size +=1

    def getSize(self):
        return self.size

    def enqueue(self,song:Music):
        index=self.size
        self.queue[index]=song
        self.increaseSize()
        
    def dequeue(self):
        if self.size==0:
            return None
        else:
            item=self.queue[0]
            self.queue=self.queue[1:]
            self.size-=1
            return item

#           title,artistname, album, duration
    #still under development
    def addtoStorage(self, name):
        """Adds the queue into the csv file
        Arguments: Name(Set a custom name for the queue)"""
        name=[[name]]
        manage=open('Library.csv', 'a',newline='') #open manager
        write= csv.writer(manage)
        write.writerows(name)
        write.writerows(self.convert()) #Adding of new data
        manage.close()   #close manager

    

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
    def convertTime(self):
        time=self.duration
        minutes, seconds = map(int, time.split(":"))
        total_seconds = minutes * 60 + seconds
        return total_seconds
    
    def getTotalDuration(self):
        """Returns total duration of the Queue"""
        """Complete this method"""
        total_seconds = 0

        for items in self.queue:
            if items is None:
                break
            minutes, seconds = map(int, items.duration.split(":"))
            total_seconds += minutes * 60 + seconds

        total_minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        return f"{total_minutes}:{remaining_seconds:02d}"
    
    def showQueue(self):
        if self.size==0:
            print("The queue is empty.")
        else:
            print("<------Songs in Queue------>")
            for i in range(self.size):
                print(f"\n{self.queue[i]}\n")
            print("<---------End of Queue--------->")
    

    def __str__(self):
        """Should return items in the queue"""
        str="<------Songs in Queue----->"
        index=0
        while index < len(self.queue):
            if self.queue[index]==None:
                break
            str+=f"\n{self.queue[index]}\n"
            index+=1
        str+="\n<---------End of Queue--------->"
        
        return str

