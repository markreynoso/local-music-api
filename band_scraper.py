"""Scrape washington band info from bandcamp."""
import json
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
    location = soup.find_all('span', class_='location')[0].text
    bio = soup.find_all('p', id='bio-text')[0].text
    links = soup.find_all('ol', id='band-links')[0].find_all('li')
    band_links_list = []
    for link in links:
        band_links_list.append(link.find('a').attrs['href'])
    img = soup.find_all('a', class_='popupImage')[0].find('img').attrs['src']
    with open('./band_data.json') as f:
        data = json.load(f)
        if artist_name not in data:
            data[artist_name] = {'albums': [(album, img)],
                                 'location': location,
                                 'styles': genre_list,
                                 'wesites': band_links_list,
                                 'bio': bio
                                 }
        else:
            data[artist_name]['albums'].append((album, img))
            for style in genre_list:
                if style not in data[artist_name]['styles']:
                    data[artist_name]['styles'].append(style)
        with open('./band_data.json', 'w') as file:
            json.dump(data, file)


all_bands_url_generator()
