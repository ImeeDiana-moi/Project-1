import csv
from Queue import Queue
from PlayList import PlayList
from Track import Track

# with open('Storage.csv', 'r') as storage:
#     read=csv.reader(storage)
#     # next(read) #skipping the track format guide
#     for lines in read:
#         print(lines)
    # with open('newstorage.csv', 'w') as manager:
    #     writer = csv.writer(manager)


#csv manager
manage=open('Storage.csv', 'a', newline='') #open manager
write= csv.writer(manage)
# write.writerows(data) #Adding of new data
manage.close()   #close manager

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


#specific printing
def getSongDetails(self, name):
    artist=name
    with open('Storage.csv', 'r') as storage:
        read=csv.reader(storage)
        for lines in read:
            # print(lines[1])
            if artist in lines[1]:
                return(f"Title: {lines[0]}\nArtist: {lines[1]}\nAlbum: {lines[2]}\nDuration: {lines[3]}")
            
def time_to_seconds(time_str):
    # Split the string into minutes and seconds
    minutes, seconds = map(int, time_str.split(":"))
    # Convert the total time to seconds
    total_seconds = minutes * 60 + seconds
    return total_seconds

# Example usage
# time_string = "2:39"
# result = time_to_seconds(time_string)
# print(f"{time_string} is equal to {result} seconds.")

# #Music.py Tests 
# m0=Music("Rap God", "Eminem"," 2:00","Niga")
# print(m0.convertTime())
# print(m0.getDuration())
# print(m1.getDuration())
# m1.convertduration()
# print(m1.getSongDetails("Break"))
# print(m0)

# song1 = Music("Libre Sampak", "No Pets Allowed", 225, "Ha")

# print(f"Title: {song1.getTitle()}")
# print(f"Artist: {song1.getArtist()}")
# print(f"Album: {song1.getAlbum()}")
# print(f"Duration: {song1.getDuration()}")




#PlayListTests
p1=PlayList()
# p1.getByArtist("Ariana Grande")
# print(p1.getByArtist("Ariana Grande"))
# print(p1.getByAlbum("The Fame Monster"))
# liste=p1.getByArtist("Ariana Grande")
# p1.createPlaylist(liste)
# print(p1.createPlaylist(liste))


#Queue.py Tests
# q1=Queue()
# m1=Music("Gangnam Style", "PSY", "4:00", "None")
# m2=Music("Gale", "PSY", "4:00", "None")
# m3=Music("Nigga Style", "PSY", "4:00", "None")
# m4=Music("Haya Style", "PSY", "4:00", "None")
# q1.enqueue(m1)
# q1.enqueue(m2)
# q1.enqueue(m3)
# q1.enqueue(m4)
# print(q1)
# q1.addtoStorage("PlayList")
# print(q1.getContent())
# print(q1.getContent())
# print(q1.convert())

# manage=open('Storage.csv', 'a', newline='') #open manager
# read=csv.reader(manage)
# write= csv.writer(manage)
# for i in read:
#     print(i)
# # write.writerows(data) 
# manage.close()


# def addtoLibrary():
    
#     title=input("Enter Title: ")
#     artist=input("Enter Artist: ")
#     album=input("Enter Album: ")
#     duration=input("Enter Duration: ")
#     data=[[title,artist,album,duration]]
#     with open("Storage.csv", mode="r",newline='') as reader:
#         read=csv.reader(reader)
#         for i in read:
#             if data[0][0] in i[0]:
#                 print('Naa na')
#                 break
#             else:
#                 manage=open('Storage.csv', 'a',newline='')
#                 write=csv.writer(manage)
#                 write.writerows(data) 
#                 manage.close()
#                 break
    
    
# data=[["title","artist","album","duration"]]
# with open("Storage.csv", mode="r",newline='') as reader:
#     read=csv.reader(reader)
    

# addtoLibrary()
        
# with open("Playlists.csv", mode='r', newline='') as reader:
#     read=csv.reader(reader)
#     count=0
#     for i in read:
#         count+=1
#     print(count)

# PlaylistName,title,artist,album,duration

# with open("Playlists.csv", mode="r", newline='') as reader:
#     read=csv.reader(reader)
#     for items in read:
#         print(f"Items: {items[0]},{items[1]},{items[2]},{items[3]}")

   # TotalDuration = 0
        # for track in self.storage0:
        #     if track is None:
        #         continue 
        #     duration = track[4]
        #     minutes, seconds = duration.split(":")  
        #     TotalDuration += int(minutes) * 60 + int(seconds)  
        
        # Total_Minutes = TotalDuration // 60
        # total_Seconds = TotalDuration % 60
        # result = f"{Total_Minutes}mins {total_Seconds:02d}s"
        # return result
    
    # def convert(self):
    #     """Convert content into list"""
    #     s=[]
    #     for items in self.storage0:
    #         if items == None:
    #             break
    #         s +=[[items[0],items[1],items[2],items[3],items[4]]]
    #     return s
    
    
    # def showplaylists(self,name, mode):
    #     """Shows playlist (specific or all)
    #     Mode: 'all'-show all playlists, 'cus'-show specific playlist"""
    #     with open('Playlists.csv',mode='r',newline='') as playlist:
    #         read=csv.reader(playlist)
    #         songs=f'<-----{name}----->\n'
    #         if mode == 'all':
    #             for items in read:
    #                 songs+=f'\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}\n'
    #         elif mode == 'cus':
    #             for items in read:
    #                 if items[0]==name:
    #                     songs+=f'\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}\n'

    #         songs+='<----End----->'
    #         print (songs)

    # def listplaylists(self):
    #     with open('Playlists.csv',mode='r',newline='') as playlist:
    #         read=csv.reader(playlist)
    #         all=[]
    #         iter=1
    #         for lists in read:
    #             if lists[0] not in all:
    #                 all+=[lists[0]]
    #         plays=f"<-----Playlists----->\n"  
    #         for items in all:
    #             plays+=f"[{iter}] {items}\n" 
    #             iter+=1  

    #         plays+="<-----End----->"   
    #         print(plays)
    #         return all
            
    # def addPlaylist(self,name):
    #     with open("Library.csv",mode='r',newline='') as reader:
    #         read=csv.reader(reader)
    #         library=[]
    #         counter=1
    #         for items in read:
    #             library+=[items]
    #             print(f"[{counter}] {items[0]}")
    #             counter+=1
    #         while True:
    #             try:
    #                 index=int(input("Enter Track Number(0 to Finish): "))
    #             except ValueError:
    #                 print("Invalid Input. Please Enter a number.")
    #                 continue
    #             if index ==0:
    #                 break
    #             elif index >= len(library):
    #                 print("Invalid! Choose again!")
    #                 continue
    #             pl=open('Playlists.csv',mode='r',newline='')
    #             reada=csv.reader(pl)

    #             data=[[name]+library[index-1]]
                
    #             manage=open('Playlists.csv', 'a',newline='')
    #             write= csv.writer(manage)
    #             write.writerows(data)
    #             manage.close()



     # def playlistbypage(self):
    #     page=1
    #     if self.getSize()!=0:
    #         plist=f'Playlist Name: {self.getPlaylistName()}\nTotal Duration: {self.getTotalDuration(self.storage0)}\nTracks:\n'
    #         counter=1
    #         maxpage=1
    #         for songs in self.storage0:
    #             plist+=f'[{counter}] {songs[1]}\n'
    #             counter+=1
    #         if counter > 6:
    #             maxpage+=1
    #         plist+=f"Page {page} of {maxpage}"
    #         return plist
    #     else:
    #         return "Nothing In playlist"
    # def playlistbypage(self, page=1, items_per_page=5):
    #     """
    #     Displays the list of playlists with pagination.

    #     Args:
    #         playlists (list[str]): List of playlist names.
    #         page (int): Current page number.
    #         items_per_page (int): Number of playlists to display per page.
    #     """
    #     playlists=self.storage0
    #     total_playlists = len(playlists)
    #     total_pages = (total_playlists + items_per_page - 1) // items_per_page  # Ceiling division

    #     # Validate and adjust the current page
    #     page = max(1, min(page, total_pages))

    #     # Calculate the range of playlists to display
    #     start_index = (page - 1) * items_per_page
    #     end_index = min(start_index + items_per_page, total_playlists)
    #     playlists_to_display = playlists[start_index:end_index]

    #     print("\n<----- Playlists ----->")
    #     for idx, playlist in enumerate(playlists_to_display, start=start_index + 1):
    #         print(f"[{idx}] {playlist}")

    #     print(f"\n<Page {page} of {total_pages}>\n[11] Previous Page\n[12] Next Page\n[0] Exit to Main Menu")

    #     return page


# pl=open('Playlists.csv',mode='r',newline='')
# read=csv.reader(pl)
# for i in read:
#     print(i)
# pl=PlayList()
# # print(pl.playlistbypage())
# prinat=pl.loadplaylist("my playlist")
# pl.addtoPlaylist(prinat)
# pl.addtoPlaylist(prinat)
# pl.addtoPlaylist(prinat)
# # # print(pl.getPlaylistName())
# pl.playlistbypage()
# pl.playlistbypage(2)
# pl.playlistbypage(3)
# pl.addtoPlaylist(pl.getBy("Ariana Grande","ar"))
# # print(pl)
# # pl.addtoStorage("Imee")
# print(pl.findcustomplaylist("Imee"))
# # print(pl.getBy("Ariana Grande",'ar'))
# # pl.addtoPlaylist(pl.getBy("Ariana Grande",'ar'))
# # # print(pl.convert())
# # # print(pl.addtoStorage("Custom"))
# # pl.addtoStorage("FUck Yeah")
# pl.findcustomplaylist("Imee")
# print(pl.addtoPlaylist(pl.getByAlbum("1989")))
# print(pl)
# print(pl.getTotalDuration(pl.getByArtist("Ariana Grande")))

# pl.addtoPlaylist([
#     ["Ahank U Next", "Ariana Grande", "Thank U Next", "3:27"],
#     ["CRings, Ariana Grande", "Thank U Next", "2:58"],
#     ["Break Free", "Ariana Grande", "My Everything, 3:34"]
# ])

# print(pl.arrangeAlphabetically(pl.storage0))




    

        
    # def getBy(self, value, mode):
    #     """Get playlist based on value(either by title, artist, or album), 
    #     Mode: tr- individual track, ar- by artist, al by album"""
    #     with open('Library.csv', 'r') as storage:
    #             read=csv.reader(storage)
    #             if mode == "tr":
    #                 s=[]
    #                 for lines in read:
    #                     if value in lines[0]:
    #                         t=[lines[[0],lines[1],lines[2],lines[3]]]
    #                         s+=[t]
    #                 return s
    #             elif mode == "ar":
    #                 s=[]
    #                 for lines in read:
    #                     if value in lines[1]:
    #                         t=[lines[0],lines[1],lines[2],lines[3]]
    #                         s+=[t]
    #                 return s
    #             elif mode == "al":
    #                 s=[]
                    
    #                 for lines in read:
    #                     if value in lines[2]:
    #                         t=[lines[0],lines[1],lines[2],lines[3]]
    #                         s+=[t]
    #                 return s
    #             return "Nothing"
    
    
    # def addtoStorage(self, name):
    #     """Adds the Playlist into the csv file
    #     Arguments: Name(Set a custom name for the queue)"""
    #     data=[]
    #     for items in self.convert():
    #         data+=[[name,items[0],items[1],items[2],items[3]]]

    #     manage=open('Playlists.csv', 'a',newline='')
    #     write= csv.writer(manage)
    #     write.writerows(data)
    #     manage.close()
    
    # def arrangeAlphabetically(self, playlist): #Bonuss
    #     """Arranges the received Playlist Alphabetically
    #     List: list from getBy() methods
    #     Returns alphabeticalized List of Songs but still follows the format"""
        
    #     Arranged = [track for track in self.storage0 if track is not None]
    #     word = len(Arranged)

    #     for i in range(word):
    #         for j in range (0, word - i - 1):
    #             if Arranged[j][0] > Arranged[j+1][0]:
    #                 Arranged[j], Arranged[j+1] = Arranged[j+1], Arranged[j]
    #     return f"Sorted Playlist \n{Arranged}"
 
    # def findcustomplaylist(self, name): #need improvement
    #     with open("Playlists.csv", mode='r',newline='') as reader:
    #         read=csv.reader(reader)
    #         plays=f"<-----{name}----->"
    #         for items in read:
    #             if items[0]==name:
    #                 plays+=f"\nTitle: {items[1]}\nArtist: {items[2]}\nAlbum: {items[3]}\nDuration: {items[4]}"
                
    #         return plays



#     def paginate_items(items, max_per_page=10):
#         """
#         Function to paginate items with navigation between pages.

#         Args:
#             items (list): List of items to paginate.
#             max_per_page (int): Maximum number of items per page.

#         Returns:
#             None
#         """
#         total_pages = (len(items) + max_per_page - 1) // max_per_page  # Calculate total pages
#         current_page = 1

#         while True:
#             # Calculate start and end indices for the current page
#             start_idx = (current_page - 1) * max_per_page
#             end_idx = start_idx + max_per_page

#             # Get items for the current page
#             page_items = items[start_idx:end_idx]

#             # Display the items
#             for idx, item in enumerate(page_items, start=start_idx + 1):
#                 print(f"{idx} {item}")
#             print(f"Page {current_page} of {total_pages}")

#             # Navigation prompt
#             print("\nNavigate: [n]ext page, [p]revious page, [q]uit")
#             choice = input("Enter your choice: ").strip().lower()

#             if choice == "n" and current_page < total_pages:
#                 current_page += 1
#             elif choice == "p" and current_page > 1:
#                 current_page -= 1
#             elif choice == "q":
#                 print("Exiting pagination.")
#                 break
#             else:
#                 print("Invalid choice or no more pages in that direction.\n")

# # Example usage
# items = [f"Item {i}" for i in range(1, 101)]  # Create a list of items
# paginate_items(items)
# import LibraryManager
# manager=LibraryManager
# # manager.loadLibrary()
# list=manager.Library
# def paginate_items(items, max_per_page=10):
#     """
#     Function to paginate items with navigation between pages.

#     Args:
#         items (list): List of items to paginate.
#         max_per_page (int): Maximum number of items per page.

#     Returns:
#         None
#     """
#     total_pages = (len(items) + max_per_page - 1) // max_per_page  # Calculate total pages
#     current_page = 1

#     while True:
#         # Calculate start and end indices for the current page
#         start_idx = (current_page - 1) * max_per_page
#         end_idx = start_idx + max_per_page

#         # Get items for the current page
#         page_items = items[start_idx:end_idx]

#         # Display the items without using enumerate
#         index = start_idx + 1
#         for item in page_items:
#             print(f"{index} {item}")
#             index += 1
#         print(f"Page {current_page} of {total_pages}")

#         # Navigation prompt
#         print("\nNavigate: [n]ext page, [p]revious page, [q]uit")
#         choice = input("Enter your choice: ").strip().lower()

#         if choice == "n" and current_page < total_pages:
#             current_page += 1
#         elif choice == "p" and current_page > 1:
#             current_page -= 1
#         elif choice == "q":
#             print("Exiting pagination.")
#             break
#         else:
#             print("Invalid choice or no more pages in that direction.\n")

# Example usage
# items = [f"{i}" for i in list]  # Create a list of items
# paginate_items(list)

# def shuffle_list():
#     # Make a copy to avoid modifying the original list
#     shuffled = [:]
#     n = len(shuffled)
    
#     for i in range(n - 1, 0, -1):
#         random_index = (i * 123456789) % (i + 1)
#         shuffled[i], shuffled[random_index] = shuffled[random_index], shuffled[i]
    
#     return shuffled

# # Example usage
# original_list = [1, 2, 3, 4, 5]
# shuffled_list = shuffle_list(original_list)
# print("Original List:", original_list)
# print("Shuffled List:", shuffled_list)

# import os

# # Specify the path to your CSV file
# file_path = 'saved_queue.csv'

# try:
#     # Check if the file exists
#     if os.path.exists(file_path):
#         # Open the file in write mode to clear its contents
#         with open(file_path, 'w') as file:
#             pass  # This clears the file
#         print(f"The contents of '{file_path}' have been deleted.")
#     else:
#         print(f"The file '{file_path}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")