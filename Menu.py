import csv
from Queue import Queue, loadTracksToQueue
from PlayList import PlayList
from Track import Track
import LibraryManager

main={
    1:"Playlists",
    2:"Music Library",
    0:"Quit"
}
# menu1={
#     1:"My Playlists",
#     0:"Return"
# }
playlists = {
    1:"Play Playlist",
    2:"Add Tracks to Playlist",
    0:"Return"
}
commands={
    1:"Next",
    2:"Previous",
    3:"Turn ON Repeat",
    4:"Turn OFF Repeat",
    5:"Shuffle Queue",
    6:"Clear Queue",
    0:"Return"
}
library={
    1:"Play Library",
    2:"Add Tracks to Library",
    0:"Return"
}

def printmenu(menu):
    for items in menu:
        if items == 11:
            print("< page 1 0f 1 >")
        print(f"[{items}] {menu[items]}")


line1 = "<---Welcome to Python Music Player--->"

if __name__ == "__main__":
    manager=LibraryManager
<<<<<<< HEAD
    # print(manager.Library)
    # for i in manager.Library:
    #     print(i)
    printmenu()
=======
    while True:
        printmenu(main)
        choice1 = input("Enter Choice: ")
        if choice1 == "1":
            while True:
                print("Playlist")
                printmenu(playlists)
                choicepl = input("Enter Choice: ")
                if choicepl == "1":
                    """Select Playlist"""
                elif choicepl == "2":
                    """Add tracks to Playlist"""
                elif choicepl == "0":
                    break

        elif choice1 == "2":
            manager.showLibrary()
            while True:
                printmenu(library)
                choicelib = input("Enter Choice: ")
                if choicelib == "1":
                    """Play Library"""
                    while True:
                        printmenu(commands)
                        choicelib1 = input("Enter Choice")
                        if choicelib1 == "1":
                            """Next track"""
                        elif choicelib1 == "2":
                            """Previous"""
                        elif choicelib1 == "3":
                            """Turn ON Repeat"""
                        elif choicelib1 == "4":
                            """Turn OFF Repeat"""
                        elif choicelib1 == "5":
                            """Shuffle Queue"""
                        elif choicelib1 == "6":
                            """Clear Queue"""
                        elif choicelib1 == "0":
                            break

                elif choicelib == "2":
                    """Add Tracks"""
                elif choicelib == "0":
                    break
        elif choice1 == "0":
            exit


>>>>>>> 2c1a5e3a923524fdc49375af2b38d2218f2921ee
