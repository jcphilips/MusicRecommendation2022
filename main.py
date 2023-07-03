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