import csv


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