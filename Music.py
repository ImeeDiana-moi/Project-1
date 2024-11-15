class Music:
    """Receives information of a song"""
    
    def __init__(self, title, artist, album, duration):
        self.title=title
        self.artist=artist
        self.album=album
        self.duration=duration


    def __str__(self):
        return f"{self.title},{self.artist},{self.album},{self.duration}"