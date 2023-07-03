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
    albums = Graph()

    for genre in genres.genres:
        albums.add_vertex(Vertex(genre))
        
    with open(data_file, 'r') as f:
        data = f.read()
        
    album_data = json.loads(data)

    for entry in album_data:
        album_vertex = Vertex(create_album(entry))
        albums.add_vertex(album_vertex)
        
        for genre in entry['genres']:
            albums.add_edge(albums.graph_dict[genre], album_vertex)

def create_album(data):
    artist =        data['artist']
    album_title =   data['album_title']
    genres =        data["genres"]
    label =         data["label"]
    rating =        data["rating"]
    review =        data['review']
    
    album = Album(album_title, artist, genres, label, rating, review)
    return album

def main():
    user_input = input("Enter a genre of album you would like to check out: ")
    print()
    try:
        genre = genres.search(user_input)
        if genre == None:
            raise ValueError('Not a valid genre')
    except ValueError as error:
        print(f'{error}. Try again!')
        main()

if __name__ == '__main__':
    introduction()
    generate_graph()
    main()