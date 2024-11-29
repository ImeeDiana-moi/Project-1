import csv
from Queue import Queue, loadTracksToQueue
from PlayList import PlayList
from Track import Track
import LibraryManager

main={
    1:"View Queue",
    2:"Playlists",
    3:"Add Tracks",
    4:"Music Library",
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
    0:"Return"
}
commands={
    1:"Play",
    2:"Next",
    3:"Previous",
    4:"Turn Off Repeat",
    5:"Turn ON Repeat",
    6:"Clear Queue",
    7:"Shuffle Queue",
    0:"Return"
}
add={
    1:"Add to Library",
    2:"Add to Playlist",
    0:"Return"
}

def printmenu(menu):
    for items in menu:
        if items == 11:
            print("< page 1 0f 1 >")
        print(f"[{items}] {menu[items]}")


line1 = "<---Welcome to Python Music Player--->"

if __name__ == "__main__":
    # Setting up library manager
    manager=LibraryManager
    # print(manager.Library)
    # for i in manager.Library:
    #     print(i)
    printmenu()