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

    def getSize(self):
        return self.size

    def enqueue(self,song:Music):
        # print(self.getSize())
        index=self.size
        self.queue[index]=song
        self.increaseSize()
        # print(self.getSize())
        
    def dequeue(self):
        pass

    # def getContent(self):
        
        
    #     # for items in self.queue:
    #     #     s+=items
            
    #     # return s

    def __str__(self):
        """Should return items in the queue"""
        str="Songs in Queue"
        index=0
        while index < len(self.queue):
            if self.queue[index]==None:
                break
            str+=f"\n{self.queue[index]}"
            index+=1
        
        return str
        

q1=Queue()
m1=Music("Gangnam Style", "PSY", "None", "4:00")
m2=Music("Gale", "PSY", "None", "4:00")
m3=Music("Nigga Style", "PSY", "None", "4:00")
m4=Music("Haya Style", "PSY", "None", "4:00")
q1.enqueue(m1)
q1.enqueue(m2)
q1.enqueue(m3)
q1.enqueue(m4)
print(q1)
# q1.getContent()
# print(q1.getContent())