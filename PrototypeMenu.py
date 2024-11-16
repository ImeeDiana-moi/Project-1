#Prototype menu for project 1, no methods yet

#imports
from time import sleep
import sys
import csv
from Queue import Queue
from PlayList import PlayList
from Music import Music

#Pre made menus
# menu1={"m1":{1:"My Playlist",
#     2: "Ariana Grande",
#     3: "Lady Gaga",
#     4: "Taylor Swift",
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
    4: "Taylor Swift",
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
    for items in menu:
        if items == 11:
            print("< page 1 0f 1 >")
        print(f"[{items}] {menu[items]}")

line1 = ["<---Welcome to Python Music Player--->"]

if __name__ == "__main__":
    player= PlayList()
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