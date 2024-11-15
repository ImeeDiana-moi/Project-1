import csv
import ArrayList
from Music import Music

class Queue:
    """Creates a Queue"""
    
    def __init__(self,size:int=50):
        self.queue=[None]*size
        self.size=0

    def increaseSize(self):
        self.size +=1

    def enqueue(self,song:Music):
        index=self.size
        self.queue[index]=song
        self.increaseSize()
        
    def dequeue(self):
        pass

    def getContent(self):
        """Should return items in the queue"""
        for items in self.queue:
            if items == None:
                break
            return items

    def __str__(self):
        return "Yes"
        

q1=Queue()
m1=Music("Gangnam Style", "PSY", "None", "4:00")
m2=Music("Gale", "PSY", "None", "4:00")
m3=Music("Nigga Style", "PSY", "None", "4:00")
m4=Music("Haya Style", "PSY", "None", "4:00")
q1.enqueue(m1)
q1.enqueue(m2)
q1.enqueue(m3)
q1.enqueue(m4)

print(q1.getContent())