import csv
from Track import Track

Library = []


def loadLibrary():
    with open("Library.csv", mode = "r", newline="") as reader:
        read = csv.reader(reader)

        for track in read:
            trackobject = Track(track[0],track[1],track[2],track[3])
            Library.append(trackobject)
    reader.close()


def showLibrary():
    s= "<-----Music Library----->\n"
    for track in Library:
        s += str(track) + "\n"
    print(s)




loadLibrary()    
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


# def addtoLibrary():
#     data=[
#         [input("Enter Title: "),
#         input("Enter Artist: "),
#         input("Enter Album: "),
#         input("Enter Duration: ")],
#     ]
#     with open('Storage.csv', 'r') as storage:
#         read=csv.reader(storage)
#         for lines in read:
#             if data[0][0] in lines[0]:
#                 print("Break")
#         manage=open('Playlists.csv', 'a', newline='')
#         write= csv.writer(manage)
#         write.writerows(data) 
#         manage.close()
