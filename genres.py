genres = ["Rock", "Experimental", "Rap", "Jazz", "Electronic", "Pop/R&B", "Folk/Country"]

def search(user_input:str):
    """Match user input to genre from whitelist

    Args:
        user_input (str): text to match to whitelist

    Returns:
        genre (str): returns genre if true, None if false
    """    
    if len(user_input) < 3:
        raise ValueError("You must enter the first 3 characters of a genre to search")
    user_input = user_input.lower().strip()
    for genre in genres:
        if user_input.startswith(genre.lower()):
            print(f"You have selected {genre}!")
            return genre
    return None
