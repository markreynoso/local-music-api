"""Scrape washington band info from bandcamp."""
from urllib.request import urlopen

from bs4 import BeautifulSoup as BS


def all_bands_url_generator():
    """Create url for each page of local results."""
    page = 0
    base_url = 'https://bandcamp.com/tag/washington?page={}'.format(page)
    for _ in range(10):
        page += 1
    one_album_url_generator(base_url)


def one_album_url_generator(bands_list_url):
    """Create url for each individual album page."""
    page = urlopen(bands_list_url)
    soup = BS(page, 'html.parser')
    albums = soup.find_all('div', class_='itemtext')
    for album in albums:
        format_url = album.text.replace(' ', '-')
        album_base_url = 'https://radicaldreamland.bandcamp.com/album/{}'.format(format_url)
        scrape_album_page(album_base_url, album.text)


def scrape_album_page(album_url, album):
    """Scrape data from album page to populate json."""
    page = urlopen(album_url)
    soup = BS(page, 'html.parser')
    artist_data = soup.find_all('div', id='name-section')
    artist_name = artist_data[0].find_all('a')[0].text
    genres = soup.find_all('a', class_='tag')
    genre_list = []
    for genre in genres:
        genre_list.append(genre.text)
    print(artist_name)
    print(album)
    print(genre_list)
    import pdb; pdb.set_trace()

all_bands_url_generator()
