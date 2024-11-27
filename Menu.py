import csv
from Queue import Queue, loadTracksToQueue
from PlayList import PlayList, addPlaylist, showplaylists,listplaylists,loadplaylist
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
    7:"Exit"
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
    manager=LibraryManager
    playlist= PlayList()
    queue=Queue()
    while True:
        print(line1)
        printmenu(main)
        try:
            first=int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Input. Please Enter a number.")
            continue

        if first == 1: #view queue
            while True:
                queue.playTrack()
                break
            
        elif first == 2: # View Playlists
            print()
            printmenu(menu1)
            try:
                p=int(input("Enter Choice: "))
            except ValueError:
                print("Invalid Input. Please Enter a number.")
                continue

            if p == 1: #show playlists
                while True:
                    with open('Playlists.csv', mode='r',newline='') as reader:
                        read=csv.reader(reader)
                        count=0
                        for i in read:
                            count+=1
                        if count == 0: #if no playlists
                            print("\nYou have no Playlists!\n[1] Create New Playlist\n[0] Return")
                            two=input("Enter Choice: ")
                            if two == "1":
                                name=input("\nEnter Playlist Name: ")
                                choose=input("\nAdd Songs to your Playlist\n[1] Choose from Library\n[2] Add Custom Track\n[0] Return")
                                if choose=='1':#choose from library
                                    addPlaylist(name)
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
                        #kani pwede
                        # elif count !=0: #If there are playlists
                        #     print()
                        #     lists=listplaylists()
                        #     try:
                        #         shu=int(input("[1] Choose Playlist\n[2] Create Another Playlist\n[0] Return\nEnter Choice: "))
                            
                        #     except ValueError:
                        #         print("Invalid Input. Please Enter a number.")
                        #         continue
                        #     if shu==1:  
                        #         chois=int(input("Enter Playlist Number: ")  )
                        #         name=lists[chois-1]
                        #         showplaylists(name,'cus')
                        #         while True:
                        #             play=int(input("[1] Play\n[2] Next\n[3] Prev\n[4] Repeat ON\n[5] Repeat OFF\n[0] Return\nEnter Choice: "))
                        #             if play == 1:
                        #                 if queue.getSize()==0:
                        #                     playlist.addtoPlaylist(loadplaylist(name))
                        #                     queue.listEnqueue(playlist.convert())
                        #                     queue.playTrack()
                        #             elif play == 2:
                        #                 queue.skipTrack()
                        #             elif play == 3:
                        #                 queue.prevTrack()
                        #             elif play == 4:
                        #                 queue.repeat = True
                        #             elif play == 5:
                        #                 queue.repeat = False
                        #             elif play==0:
                        #                 break

                            elif shu==2:
                                name=input("\nEnter Playlist Name: ")
                                choose=input("\nAdd Songs to your Playlist\n[1] Choose from Library\n[2] Add Custom Track\n[0] Return")
                                if choose=='1':#choose from library
                                    addPlaylist(name)

                            elif shu==0:
                                break
                            else:
                                continue
            #show premade playlists by artist 
             
            #kani pwede  
            # elif p ==2:
            #     playlist.addtoPlaylist(playlist.getBy(menu1[p], 'ar'))
            #     queue.listEnqueue(playlist.convert())
                
                

            else:
                continue





        elif first == 3: # Add Tracks
            while True:
                printmenu(add)
                three=int(input("Enter Choice: "))
                if three==1:
                    manager.addtoLibrary()
                    
                elif three == 2:
                    pass
                elif three==0:
                    break
                else:
                    continue

        elif first == 4: # Add Playlist
            while True:
                manager.showLibrary()
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
                elif choice == 7:
                    break
                else:
                    continue
                    



            

        elif first==0: # Quit
            break

        else:
            continue