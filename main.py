from vertex import Vertex
from graph import Graph
from album import Album
import genres
import json

def introduction():
    print("""▓████▓▓█▓▒░░░▓▓▓░░░░░░░░░░░░░░░░▒▓▓█▓░░░░░░░░░░▒▓▓▓██▒░░░░░░░░░░░░░░▒▓▓██░░░░░░░
░▓███░░░███░░███░░░░▓▓░░░░░░░░░░░▓███░░░░░░░░░██▓░░▓█░░░░░░░░░░░░░░░░▓███░░░░░░░
░▓███░░░███▓▒▓▓█░▒▓███▒▒░░▒▓▓█▓▓░▓███▒▓█▓▒░░░▓███▒▒░▒▓▓▓▓▓▒░░▒▒▓▓░▓█▒▓███░▒▓▓▓▓░
░▓███▒▒▓██▒░▒███░░███▓░░░██░░░██░▓███░░███▒░░▒███░░▓██▓░▒███▒▓██████▒▓███░░▓█▓░░
░▓███▒▒░░░░░░███░░▓██▓░░▓██░░░░░░▓██▓░░███▓░░▒███░░███▒░▒███▒░███▒░░░▓███▓██▓░░░
░▓███░░░░░░░░███░░▓██▓░░▓██▓▒▒▒▓░▓██▓░░███▓░░▒███░░███▓░▒███░░███░░░░▓███░████▒░
▓█████▓░░░░▒▓████▒▒████▓░▒█████▒▓████▒▒████▓▒████▓░░▓██▒██▓░░▓████▒░▒████▒░▓███▓
""")
    print("Welcome to Pitchfork's Best of 2022!")
        
def generate_album_graph(data_file):
    """Generate graph using album data from a provided JSON.

    Args:
        data_file (json): JSON file containing album information.

    Returns:
        albums (Graph): Returns a graph whose vertices are genres and their edges are albums. 
    """    
    albums = Graph()

    # create vertices for all valid genres and add them to the graph
    for genre in genres.genres:
        albums.add_vertex(Vertex(genre))
        
    with open(data_file, 'r') as f:
        data = f.read()
    
    # parse JSON file
    album_data = json.loads(data)

    # create an album vertex and make graph connections for every entry in the json
    for entry in album_data:
        album_vertex = Vertex(create_album(entry))
        albums.add_vertex(album_vertex)
        
        for genre in entry['genres']:
            albums.add_edge(albums.graph_dict[genre], album_vertex)
            
    return albums

def create_album(data):
    """Creates an Album object

    Args:
        data (dict): variable containing data to create an album object

    Returns:
        album (Album): Returns Album object
    """    
    artist =        data['artist']
    album_title =   data['album_title']
    genres =        data["genres"]
    label =         data["label"]
    rating =        data["rating"]
    review =        data['review']
    
    album = Album(album_title, artist, genres, label, rating, review)
    return album

def display_album(album):
    """Prints out album information from an Album object.

    Args:
        album (Album): Album object to print information from.
    """    
    print(f"\n\nAlbum Title:        {album.album_title}")
    print(f"Artist:             {album.artist}")
    print(f"Genres:             {', '.join(album.genres)}")
    print(f"Label:              {album.label}")
    print(f"Pitchfork Rating:   {album.rating}")
    print(f"Pitchfork Review:   {album.review}\n\n")

def main():
    
    # print out list of valid genres
    print(f"\nGenres: {', '.join(genres.genres)}")
    user_input = input("Enter a genre you would like to check out: ")
    print()
    
    # handle inputs
    try:
        genre = genres.search(user_input)
        if genre == None:
            raise ValueError('Not a valid genre')
    except ValueError as error:
        print(f'{error}. Try again!')
        return main()
    
    # select genre and display albums of selected genre
    genre_vertex = albums.graph_dict[genre]
    print(f"\nThese are Pitchfork's top {genre} albums for 2022:\n")
    top_albums = albums.show_edges(genre_vertex)
    for key, album in top_albums.items():
        print(f"\t{key}. {album.album_title}: {album.artist}")    
    print()
    
    # select album from list to view information
    print("Enter the number of the album you would like to view, or type 'q' to quit.")
    print("Or type 's' to select a different genre.")
    
    # handle user input
    while True:
        user_input = input("Please enter a selection here: ")
        if user_input == 's':
            return main()
        if user_input == 'q':
            return
        try:
            user_input = int(user_input)
            selected_album = top_albums.get(user_input, None)
            if not selected_album:
                raise ValueError
            break
        except ValueError:
            print("Invalid input!")
    
    # print album information
    print(f"\nSeleced {selected_album.album_title}: {selected_album.artist}")
    display_album(selected_album)

    # handle user input for continuing
    user_input = ''
    while user_input == '':
        user_input = input("Do you want to quit or continue browsing?\n" 
                           "Enter 'q' to quit or 'c' to continue: ")
        if user_input == 'q':
            print("\nSee you next time!\n")
            return
        if user_input == 'c':
            return main()
        user_input = ''

if __name__ == '__main__':
    introduction()
    albums = generate_album_graph('album_data.json')
    main()
