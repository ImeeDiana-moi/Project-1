#Prototype menu for project 1, no methods yet

#imports
from time import sleep
import sys
import csv
from Queue import Queue
from ArrayList import ArrayList
from Music import Music

#Pre made menus
# menu1={"m1":{1:"My Playlist",
#     2: "Ariana Grande",
#     3: "Lady Gaga",
#     4: "Taylor Swrift",
#     5: "Nicki Minaj",
#     6: "Eminem",
#     7: "Beyonce",
#     8: "The Weekend",
#     9: "SZA",
#     10: "Frank Ocean"},
#     "pages":{11:"Next Page",
#     12:"Previous Page",},
# }
menu1={
    1:"My Playlist",
    2: "Ariana Grande",
    3: "Lady Gaga",
    4: "Taylor Swrift",
    5: "Nicki Minaj",
    6: "Eminem",
    7: "Beyonce",
    8: "The Weekend",
    9: "SZA",
    10: "Frank Ocean",
    11:"Next Page",
    12:"Previous Page",
}

#Methods
def printmenu(menu):
    index=0
    for items in menu:
        if items == 11:
            print("< page 1 0f 1 >")
        print(f"[{items}] {menu[items]}")

line1 = ["<<<Welcome to Python Music Player>>>"]

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
    #Intro with transition
    for line in line1:        
        for c in line:          
            print(c, end='')    
            sys.stdout.flush()  
            sleep(0.1)          
    print('')
    #Print Menu
    printmenu(menu1)
    first=int(input("Enter Choice: "))