import csv
from Queue import Queue, loadTracksToQueue
from PlayList import PlayList,showplaylists,createplaylist
from Track import Track
import LibraryManager

menus = {
    "main": {
        1:"Playlists",
        2:"Music Library",
        0:"Quit"
    },

    "playlists": {
        1:"Play Playlist",
        2:"Add Tracks to Playlist",
        3:"View Alphabetically",
        4:"Manage Queue",
        0:"Return"
    },

    "commands": {
        1:"Next",
        2:"Previous",
        3:"Turn ON Repeat",
        4:"Turn OFF Repeat",
        5:"Shuffle Queue",
        6:"Clear Queue",
        0:"Return"
    },

    "library": {
        1:"Play All",
        2:"Choose Track to Play",
        3:"Add Tracks to Library",
        4:"View Alphabetically",
        5:"Manage Queue",
        0:"Return"
    }
}

def printmenu(menu: str) -> None:
    assert type(menu) == str, "Invalid menu given!"
    i = 1
    for m in menus[menu].values():
        print("[{}] {}".format(i, m))
        i += 1

line1 = "<---Welcome to Python Music Player--->"

if __name__ == "__main__":
    manager=LibraryManager
    plays=PlayList()
    queue = Queue()
    while True:
        printmenu("main")
        choice1 = input("Enter Choice: ")
        if choice1 == "1":
            while True:
                val=showplaylists()
                if val is None:
                    dec = input("Would you like to create a playlist (y/n)? ")
                    if dec.lower() == 'y':
                        name = input("Enter Playlist Name: ")
                        createplaylist(name)
                        break
                    elif dec.lower() == 'n':
                        break
                    else:
                        print("Invalid Choice!")
                        continue
                ch = input("\nEnter playlist number or enter 'c' to create a new Playlist\n[0] Return\nEnter Choice: ")
                if ch == '0':
                    break
                elif ch.lower() == 'c':
                    name = input("Enter Playlist Name: ")
                    createplaylist(name)
                    break
                elif 1 <= int(ch) <= len(val):
                    selected_playlist = val[int(ch) - 1]
                    plays.getPlaylist(selected_playlist)
                    print(plays)

                    while True:
                        printmenu("playlists")
                        choicepl = input("Enter Choice: ")

                        if choicepl == "1":
                            while True:
                                plays.showTracksInPlaylist(selected_playlist)
                                choice_track = input("Enter the track number to play or [0] to return: ")

                                if choice_track == "0":
                                    break

                                if 1 <= int(choice_track) <= plays.getSize():
                                    selected_index = int(choice_track) - 1
                                    tracks_to_play = plays.storage0[selected_index:]
                                    queue.listEnqueue(tracks_to_play)
                                    print(queue.playTrack()) 
                                    break
                                else:
                                    print("Invalid choice. Please try again.")

                        elif choicepl == "2":
                            """"Add track to library and playlist"""
                            while True:
                                dec = input("Would you like to add tracks to playlist (y/n)? ")
                                if dec.lower() == 'y':
                                    name = plays.getPlaylistName()
                                    createplaylist(name) #utilize createplaylist method to add tracks to the playlist
                                    break
                                elif dec.lower() == 'n':
                                    break
                                else:
                                    print("Invalid Choice!")
                                    continue

                        elif choicepl=='3':
                            plays.showPlaylistAlpha()
                            print(plays)
                        elif choicepl == '4': #Manage Queue
                            while True:
                                if queue.getSize() == 0:
                                    print("The queue is empty. Add tracks before managing.")
                                    break
                                printmenu("commands")
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
                        elif choicepl == "0":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("Invalid Choice! Please enter a valid playlist number.")
        elif choice1 == "2":
            manager.showLibrary()
            while True:
                printmenu("library")
                choicelib = input("Enter Choice: ")
                if choicelib == "1":
                    """Play All"""
                    try:
                        if not manager.Library:
                            print("Library is empty. Add tracks to the library first.")
                        else:
                            # queue = Queue()
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

                        if 1 <= int(choicelib2) <= len(manager.Library):
                            selected_index = int(choicelib2) - 1 
                            queue.listEnqueue(manager.Library[selected_index:])
                            print(queue.playTrack())
                            break
                elif choicelib=='3':
                    while True:
                        manager.addtoLibrary()
                        again=input("Would you like to add another one(y/n)?")
                        if again == 'n':
                            break
                        elif again =='y':
                            continue
                        else:
                            print("Invalid Choice!")
                            break
                elif choicelib == '4':#Show Library alphabetically
                    manager.AlphaLibrary(manager.Library)
                elif choicelib == '5': #Manage Queue
                    while True:
                        if queue.getSize() == 0:
                            print("The queue is empty. Add tracks before managing.")
                            break
                        printmenu("commands")
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

                elif choicelib == "0":
                    break

        elif choice1 == "0":
            break
        else: 
            continue
