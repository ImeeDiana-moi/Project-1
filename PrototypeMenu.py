#Prototype menu for project 1, no methods yet

#imports
from time import sleep
import sys
import csv
from Queue import Queue
from ArrayList import ArrayList

#Pre made menus
menu1={
    1:"My Playlist",
    2:"Ed Sheeran",
    3:"Bruno Mars",
    4:"Michael Jackson",
    5:"Beyonce",
    6:"Drake",
    7:"Lewis Capaldi",
    8:"The Weeknd",
    9:"Eminem",
    10:"",
    11:"Next Page",
    12:"Previous Page",
}

#Methods
def printmenu(menu):
    for items in menu:
        print(f"[{items}] {menu[items]}")


#Start
line1 = ["<<<Welcome to Python Music Player>>>"]

#Printing with Animation
# for line in line1:        
#     for c in line:          
#         print(c, end='')    
#         sys.stdout.flush()  
#         sleep(0.1)          
#     print('')

#CSV reader
# with open('Storage.csv', 'r') as storage:
#     read=csv.reader(storage)
#     next(read) #skipping the track format guide
#     for lines in read:
#         print(lines)
    # with open('newstorage.csv', 'w') as manager:
    #     writer = csv.writer(manager)

#Sample to add
data=[
    []
]     #if adding new elements to the storage, must be in a list format
datas=[
    [],[],[]
]

#csv manager
manage=open('Storage.csv', 'a', newline='') #open manager
write= csv.writer(manage)
# write.writerows(data) #Adding of new data
manage.close()   #close manager


# playlist=ArrayList()
# print(playlist)


if __name__ == "__main__":
    player= ArrayList()
    printmenu(menu1)