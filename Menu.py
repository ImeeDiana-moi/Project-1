import csv
from Queue import Queue, loadTracksToQueue
from PlayList import PlayList,showplaylists,createplaylist,loadplaylist
from Track import Track
import LibraryManager

main={
    1:"Playlists",
    2:"Music Library",
    3:"Manage Queue",
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
    1:"Play All",
    2:"Choose Track to Play",
    3:"Add Tracks to Library",
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
                    try:
                        if not manager.Library:
                            print("Library is empty. Add tracks to the library first.")
                        else:
                            queue = Queue()
                            queue.listEnqueue(manager.Library)
                            print(queue.playTrack())
                    except Exception as e:
                        print(f"Error: {e}. The queue might be empty. Try adding tracks again.")
                elif choicelib == "2":
                    """Choose Track to Play"""
                    while True:
                        manager.showLibrary()
                        choicelib2 = input("Enter the track number to play or [0] to return: ")

                        if choicelib2 == "0":
                            break

                        if choicelib2.isdigit() and 1 <= int(choicelib2) <= len(manager.Library):
                            selected_index = int(choicelib2) - 1  # Get the selected track index
                            queue = Queue()
                            queue.listEnqueue(manager.Library[selected_index:])# Enqueue the selected track and all subsequent tracks
                            print(queue.playTrack())  # Play the selected track
                            break
                
                elif choicelib == "0":
                    break
        elif choice1 == "3":
            """Manage Queue"""
            while True:
                printmenu(commands)
                choicelib1 = input("Enter Choice: ")
                try:
                    if choicelib1 == "1":  # Next track
                        if queue.getSize() == 0:
                            print("The queue is empty. Add tracks before managing.")
                        else:
                            queue.skipTrack()
                            print(queue.playTrack())
                    elif choicelib1 == "2":  # Previous track
                        if queue.getSize() == 0:
                            print("The queue is empty. Add tracks before managing.")
                        else:
                            queue.prevTrack()
                            print(queue.playTrack())
                    elif choicelib1 == "3":  # Turn ON Repeat
                        queue.toggleRepeat()
                    elif choicelib1 == "4":  # Turn OFF Repeat
                        queue.repeat = False
                    elif choicelib1 == "5":  # Shuffle Queue
                        if queue.getSize() == 0:
                            print("The queue is empty. Add tracks before shuffling.")
                        else:
                            queue.shuffleQueue()
                    elif choicelib1 == "6":  # Clear Queue
                        queue.clearQueue()
                        print("Queue cleared.")
                    elif choicelib1 == "0":  # Return
                        break
                except NameError:
                    print("Queue is not initialized!")
                except Exception as e:
                    print(f"The Queue is Empty!")

        elif choice1 == "0":
            exit

