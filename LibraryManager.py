import csv
from Track import Track

Library = []
def loadLibrary():
    """Gets tracks from Library.csv and append to Library"""
    with open("Library.csv", mode = "r", newline="") as reader:
        read = csv.reader(reader)
        
        for track in read:
            trackobject = Track(track[0],track[1],track[2],track[3],track[4])
            Library.append(trackobject)
                
    reader.close()
    
def AlphaLibrary(Library):
    """Shows the Playist(Default: Alphabetical)"""
    if not Library or all(track is None for track in Library):
        print("The playlist is empty or invalid.")
        return
    def get_track_title(track):
        return track.gettitle().lower()
    
    Library = sorted(Library, key=get_track_title)
    print("<----Playlist in Alphabetical Order---->")
    count = 1
    for track in Library:
        print(f"[{count}] {track}")
        count += 1
    print("<-------------------------------------->"+"\n")


def showLibrary():
    count = 1
    s= "<-----Music Library----->\n"
    for track in Library:
        s += f"[{count}]{str(track)}\n"
        count += 1
    print(s)
    
def addtoLibrary():
    """Add track to library"""
    title=input("Enter Title: ")
    artist=input("Enter Artist: ")
    album=input("Enter Album: ")
    duration=input("Enter Duration(seconds): ")
    data=[ [title,artist,album,duration]]
    manage=open('Library.csv', 'a', newline='')
    write= csv.writer(manage)
    write.writerows(data) 
    manage.close()
    print("Succesfully added track.")

def show():
    e=open('Library.csv', 'a',newline='')
    w=csv.writer(e)
    count=1
    for tracks in Library:
        print(f"[{count}] {tracks.title}")
        count+=1
    return w
        
def createplaylist(name):
    """Receives a name to create a playlist and choose tracks from library only"""
    w=show()
    while True:
        try:
            ind=int(input("Choose Tracks(0 to exit): "))
        except:
            print("Enter valid Choice.")
        
        if ind == 0:
            break
        elif ind > len(Library):
            print("Index out of range.")
            continue
        track=Library[ind-1]
        w.writerows([[track.title,track.artist,track.album,track.duration,name]])
        print("Track added!")
            
def showplaylists():
    """Prints Playlist names from Playlist csv>
    Return None if playlist.csv is empty"""
    print("\n"+"<-----Playlists----->")
    if len(Library)==0:
        print("No Playlists. Create one.\n")
        return None
    count=1
    l=[]
    for items in Library:
        if items.playlist not in l:
            if items.playlist != "None":
                l.append(items.playlist)
    for items in l:
        print(f"({count}) {items}")
        count+=1
    return l

def deletePlaylist(name):

    file_path = "Library.csv"
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        filtered_rows = [row for row in rows if row[4] != name]
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(filtered_rows)







# loadLibrary()    


# for i in Library:
#     print(i)
    # with open("Library.csv", mode='r', newline='') as reader:
    #     read=csv.reader(reader)
    #     # t = Track()
    #     for items in read:
    #         # t = Track
    #         # s+=f"\nTitle: {items[0]}\nArtist: {items[1]}\nAlbum: {items[2]}\nDuration: {items[3]}\n"
    # s+="<----End of Library----->"
    # print(s)

# def addtracktoplaylist(name):
#     data=[
#         [name],
#         [
#             input("Enter Track Title: "),
#             input("Enter Track Artist: "),
#             input("Enter Track Album: "),
#             input("Enter Track Duration(00:00): "),
#         ]
#     ]
#     w=open('Playlists.csv',mode='a',newline='')
#     writer=csv.writer(w)
#     writer.writerows(data)


# showLibrary()
# AlphaLibrary(Library)
# showLibrary()

# addtoLibrary()