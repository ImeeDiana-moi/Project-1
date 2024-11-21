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
time_string = "2:39"
result = time_to_seconds(time_string)
print(f"{time_string} is equal to {result} seconds.")

#Music.py Tests 
m0=Music("Rap God", "Eminem"," 2:00","Niga")
print(m0.convertTime())
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
q1=Queue()
m1=Music("Gangnam Style", "PSY", "4:00", "None")
m2=Music("Gale", "PSY", "4:00", "None")
m3=Music("Nigga Style", "PSY", "4:00", "None")
m4=Music("Haya Style", "PSY", "4:00", "None")
q1.enqueue(m1)
q1.enqueue(m2)
q1.enqueue(m3)
q1.enqueue(m4)
# print(q1)
# q1.addtoStorage("PlayList")
# print(q1.getContent())
# print(q1.getContent())
# print(q1.convert())