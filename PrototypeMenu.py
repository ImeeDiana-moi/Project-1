#Prototype menu for project 1, no methods yet

#imports
from time import sleep
import sys
import csv

#Pre made menus
menu1={
    1:"My Playlist",
    2:"Ed Sheeran",
    3:"Bruno Mars",
    4:"My Playlist",
    5:"My Playlist",
    6:"My Playlist",
    7:"My Playlist",
    8:"My Playlist",
    9:"My Playlist",
    10:"My Playlist",
    11:"Next Page",
    12:"Previous Page",
}

#Methods
def printmenu(menu):
    for items in menu:
        print(f"[{items}] {menu[items]}")


#Start
line1 = ["<<<Welcome to Python Music Player>>>"]
# for line in line1:        
#     for c in line:          
#         print(c, end='')    
#         sys.stdout.flush()  
#         sleep(0.1)          
#     print('')
with open('Storage.csv', 'r') as storage:
    read=csv.reader(storage)
    next(read) #skipping the track format guide
    for lines in read:
        print(lines)
    # with open('newstorage.csv', 'w') as manager:
    #     writer = csv.writer(manager)

    