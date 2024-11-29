import csv
from Queue import Queue, loadTracksToQueue
from PlayList import PlayList,showplaylists,createplaylist,loadplaylist
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

        print(f"[{items}] {menu[items]}")


line1 = "<---Welcome to Python Music Player--->"

if __name__ == "__main__":
    manager=LibraryManager
    plays=PlayList()
    while True:
        printmenu(main)
        choice1 = input("Enter Choice: ")
        if choice1 == "1":
            val=showplaylists()
            while True:
                
                if val==None:
                    dec=input("Would you like to create a playlist(y/n)?")
                    if dec =='y':
                        name=input("Enter Playlist Name:")
                        createplaylist(name)
                        loadplaylist()
                        break
                    elif dec=='n':
                        break
                    else:
                        print("Invalid Choice!")
                        continue
                ch=input("\nEnter playlist number or enter 'c' to create a new Playlist\n[0] Return\nEnter Choice: ")
                if ch=='c':
                    name=input("Enter Playlist Name:")
                    createplaylist(name)
                    loadplaylist()
                    break
                elif ch:
                    plays.getPlaylist(val[int(ch)-1])
                    print(plays)
                elif ch =='0':
                    break

        elif choice1 == "2":
            manager.showLibrary()
            while True:
                printmenu(library)
                choicelib = input("Enter Choice: ")
                if choicelib == "1":
                    """Play All"""
                    break
                elif choicelib == "2":
                    """Choose Track to Play"""
                    while True:
                        manager.showLibrary()
                        choicelib2 = input("Enter Choice: ")
                        """Play chosen Track"""
                        break
                elif choicelib == "0":
                    break
        elif choice1 == "3":
            """Manage Queue"""
            """Show Queue"""
            while True:
                printmenu(commands)
                choicelib1 = input("Enter Choice: ")
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
        elif choice1 == "0":
            exit

