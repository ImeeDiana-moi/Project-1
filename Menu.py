#Menu for project 1

#imports
from time import sleep
import sys
import csv
from Queue import Queue
from PlayList import PlayList
from Track import Track

#Pre made menus
main={
    1:"Music Library",
    2:"View Queue",
    3:"Add Tracks",
    4:"Add PLayList",
    0:"Quit"
}
menu1={
    1:"My Playlists",
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
commands={
    1:"Play",
    2:"Next",
    3:"Previous",
    4:"Turn Off Repeat",
    5:"Turn ON Repeat",
    6:"Clear Queue",
    7:"Exit"
}

#Methods
def printmenu(menu):
    for items in menu:
        if items == 11:
            print("< page 1 0f 1 >")
        print(f"[{items}] {menu[items]}")

line1 = "<---Welcome to Python Music Player--->"

#Start
if __name__ == "__main__":
    player= PlayList()
    queue=Queue()
    while True:
        print(line1)
        printmenu(main)
        try:
            first=int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Input. Please Enter a number.")
            continue

        if first == 1: # Music Library
            while True:
                printmenu(menu1)
                try:
                    one=int(input("Enter Choice: "))
                except ValueError:
                    print("Invalid Input. Please Enter a Number.")
                    continue
                if one in menu1:
                    print(f"You selected {menu1[one]}.")
                    break
                elif one == 0:
                    break
                else:
                    print("Invalid option.")

        elif first == 2: # View Queue
            while True:
                printmenu(menu1)
                one=int(input("Enter Choice: "))

        elif first == 3: # Add Tracks
            while True:
                printmenu(menu1)
                one=int(input("Enter Choice: "))

        elif first == 4: # Add Playlist
            while True:
                printmenu(menu1)
                one=int(input("Enter Choice: "))

        elif first==0: # Quit
            break

        else:
            continue