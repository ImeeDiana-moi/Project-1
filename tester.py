import csv

# with open('Storage.csv', 'r') as storage:
#     read=csv.reader(storage)
#     # next(read) #skipping the track format guide
#     for lines in read:
#         print(lines)
    # with open('newstorage.csv', 'w') as manager:
    #     writer = csv.writer(manager)


#specific printing
def getSongDetails(self, name):
    artist=name
    with open('Storage.csv', 'r') as storage:
        read=csv.reader(storage)
        for lines in read:
            # print(lines[1])
            if artist in lines[1]:
                return(f"Title: {lines[0]}\nArtist: {lines[1]}\nAlbum: {lines[2]}\nDuration: {lines[3]}")
