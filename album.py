class Album:
    def __init__(self, album_title, artist, genres, label, rating, review) -> None:
        """Constructor for an album object

        Args:
            album_title (str): Name of album
            artist (str): Name of the artist
            genres (list): List of genres associated to the album
            label (str): Name of label(s)
            rating (float): Pitchfork rating
            review (str): Pitchfork review
        """        
        self.album_title = album_title
        self.artist = artist
        self.genres = genres
        self.label = label
        self.rating = rating
        self.review = review
