import genres
from album import Albums

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


def display_results():
    pass

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
    main()