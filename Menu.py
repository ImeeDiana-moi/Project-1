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
    7:"Exit"
}
add={
    1:"Add to Library",
    2:"Add to Playlist",
    0:"Return"
}
# playLists={
#     1:"Create New Playlist",
#     0:"Return"
# }
#Methods
def printmenu(menu):
    for items in menu:
        if items == 11:
            print("< page 1 0f 1 >")
        print(f"[{items}] {menu[items]}")

def addtoLibrary():
    data=[
        [input("Enter Title: "),
        input("Enter Artist: "),
        input("Enter Album: "),
        input("Enter Duration: ")],
    ]
    with open('Storage.csv', 'r') as storage:
        read=csv.reader(storage)
        for lines in read:
            if data[0][0] in lines[0]:
                print("Break")
        manage=open('Playlists.csv', 'a', newline='')
        write= csv.writer(manage)
        write.writerows(data) 
        manage.close()

def showLibrary():
    s="<-----Music Library----->\n"
    with open("Library.csv", mode='r', newline='') as reader:
        read=csv.reader(reader)
        for items in read:
            s+=f"\nTitle: {items[0]}\nArtist: {items[1]}\nAlbum: {items[2]}\nDuration: {items[3]}\n"
    s+="<----End of Library----->"
    print(s)
line1 = "<---Welcome to Python Music Player--->"

def loadTracksToQueue(queue):
    with open('Library.csv', mode='r') as storage:
        reader = csv.reader(storage)
        for line in reader:
            if len(line) >= 4:  # Ensure all required data is present
                title, artist, album, duration = line
                track = Track(title, artist, album, duration)
                queue.enqueue(track)
    print(f"Tracks loaded into the queue from Library.csv.\n")


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
                break

        elif first == 2: # View Playlists
            # with open('Playlist.csv', mode='r',newline='') as reader:
            #     read=csv.reader(reader)
            # manager=open('Playlists.csv')
            # writer=csv.writer(manager)
            while True:
                with open('Playlists.csv', mode='r',newline='') as reader:
                    read=csv.reader(reader)
                    count=0
                    for i in read:
                        count+=1
                    if count == 0:
                        print("You have no Playlists!\n[1] Create New Playlist\n[0] Return")
                        two=input("Enter Choice: ")
                        if two == "1":
                            name=input("Enter Playlist Name: ")
                            choose=input("\nAdd Songs to your Playlist\n[1] Choose from Library\n[2] Add Custom Track\n[0] Return")
                            if choose=='1':#choose from library
                                pass
                            elif choose=='2': #add custom
                                pass

                            elif choose=='0':
                                break
                            else:
                                continue
                
                        elif two=='0':
                            break
                        else:
                            print("Invalid Choice. Try Again!")
                            continue
                    elif count !=0:
                        print("naa")
                        break
                    
        elif first == 3: # Add Tracks
            while True:
                printmenu(add)
                three=int(input("Enter Choice: "))
                if three==1:
                    addtoLibrary()
                    
                elif three == 2:
                    pass
                elif three==0:
                    break
                else:
                    continue

        elif first == 4: # Add Playlist
            while True:
                showLibrary()
                break
            while True:
                printmenu(commands)
                choice = int(input("Enter Choice: "))
                if choice == 1:  # Play Track
                    if queue.getSize() == 0:
                        print("The queue is empty. Loading tracks from Library.csv...")
                        loadTracksToQueue(queue)  # Load tracks if queue is empty
                    if queue.getSize() > 0:
                        queue.playTrack()  # Play the current track
                    else:
                        print("No tracks available to play.")
                elif choice == 2:
                    queue.skipTrack()
                elif choice == 3:
                    queue.prevTrack()
                elif choice == 4:
                    queue.repeat = False
                elif choice == 5:
                    queue.repeat = True
                    



            

        elif first==0: # Quit
            break

        else:
            continue