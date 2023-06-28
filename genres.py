genres = ["rock", "experimental", "rap", "jazz", "electronic", "pop/r&b", "folk/country"]

def search(user_input:str):
    """Match user input to genre from whitelist

    Args:
        user_input (str): text to match to whitelist

    Returns:
        genre (str): returns genre if true, None if false
    """    
    user_input = user_input.lower().strip()
    for genre in genres:
        if user_input in genre:
            return genre
    return None
