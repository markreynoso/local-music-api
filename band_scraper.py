"""Scrape washington band info from bandcamp."""
import json
from urllib.request import urlopen

from bs4 import BeautifulSoup as BS


def all_bands_url_generator():
    """Create url for each page of local results."""
    page = 0
    for _ in range(10):
        page += 1
        base_url = 'https://bandcamp.com/tag/washington?page={}'.format(page)
        print(base_url)
        one_album_url_generator(base_url)


def one_album_url_generator(results_url):
    """Create url for each individual album page."""
    page = urlopen(results_url)
    soup = BS(page, 'html.parser')
    albums = soup.find_all('li', class_='item')
    for album in albums:
        album_url = album.find('a').attrs['href']
        album = album.find('a').attrs['title']
        scrape_album_page(album_url, album)


def scrape_album_page(album_url, album):
    """Scrape data from album page to populate json."""
    page = urlopen(album_url)
    soup = BS(page, 'html.parser')
    artist_name = soup.find('div', id='name-section').find('a').text
    genres = soup.find_all('a', class_='tag')
    genre_list = []
    for genre in genres:
        genre_list.append(genre.text)
    location = soup.find('span', class_='location').text
    bio = ''
    if soup.find('p', id='bio-text'):
        bio = soup.find('div', class_='signed-out-artists-bio-text').find('meta').attrs['content']
    band_links_list = []
    if soup.find('ol', id='band-links'):
        links = soup.find('ol', id='band-links').find_all('li')
        for link in links:
            band_links_list.append(link.find('a').attrs['href'])
    img = soup.find('a', class_='popupImage').find('img').attrs['src']
    with open('./band_data.json') as f:
        data = json.load(f)
        if artist_name not in data:
            data[artist_name] = {'albums': [(album, img)],
                                 'location': location,
                                 'styles': genre_list,
                                 'websites': band_links_list,
                                 'bio': bio
                                 }
        else:
            data[artist_name]['albums'].append((album, img))
            for style in genre_list:
                if style not in data[artist_name]['styles']:
                    data[artist_name]['styles'].append(style)
        with open('./band_data.json', 'w') as file:
            json.dump(data, file)


# all_bands_url_generator()
with open('./band_data.json') as d:
    the_data = json.load(d)
    print(list(the_data['Lena Raine'].keys()))
    # for band in the_data:
        # print(the_data(band))
        # locations = []
        # locations.append(the_data[band]['location'])
        # print(sorted(locations))