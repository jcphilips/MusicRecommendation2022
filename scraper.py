import requests
from bs4 import BeautifulSoup
import json

def scrape_album_data(url):
    """Scrape album data from provided url

    Args:
        url (str): string http link to Pitchfork article

    Returns:
        Album: Returns an album object
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_tag = soup.findAll('h2')
    pitchfork_data = []
    for result in title_tag:
        title = result.text
        artist, album_title = title.split(':', 1)
        review = result.next_sibling.text
        album_data = {
            'artist': artist,
            'album_title': album_title,
            'review' : review
            }
        pitchfork_data.append(album_data)
    
    return pitchfork_data
    
def main():
    """Scrapes album data from all of the Pitchfork album review pages."""
    url = 'https://pitchfork.com/features/lists-and-guides/best-albums-2022/'
    pitchfork_data =  scrape_album_data(url)

    with open('album_data.json', 'w') as f:
        json.dump(pitchfork_data, f)

main()