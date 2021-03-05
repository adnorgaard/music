import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import csv

CLIENT_ID = '5bfbb3ff36504130b06d661d5181daaf'
CLIENT_SECRET = '9d13e9b352d8414d99a464cf939fc195'

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, 
                                        client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(auth_manager=auth_manager)

top_charts = {
              'AR': 'spotify:playlist:37i9dQZEVXbMMy2roB9myp',
              'BO': 'spotify:playlist:37i9dQZEVXbJqfMFK4d691',
              'BR': 'spotify:playlist:37i9dQZEVXbMXbN3EUUhlg',
              'CO': 'spotify:playlist:37i9dQZEVXbOa2lmxNORXQ',
              'CL': 'spotify:playlist:37i9dQZEVXbL0GavIqMTeb',
              'CR': 'spotify:playlist:37i9dQZEVXbMZAjGMynsQX',
              'DO': 'spotify:playlist:37i9dQZEVXbKAbrMR8uuf7',
              'EC': 'spotify:playlist:37i9dQZEVXbJlM6nvL1nD1',
              'SV': 'spotify:playlist:37i9dQZEVXbLxoIml4MYkT',
              'GT': 'spotify:playlist:37i9dQZEVXbLy5tBFyQvd4',
              'HN': 'spotify:playlist:37i9dQZEVXbJp9wcIM9Eo5',
              'MX': 'spotify:playlist:37i9dQZEVXbO3qyFxbkOE1',
              'NI': 'spotify:playlist:37i9dQZEVXbISk8kxnzfCq',
              'PA': 'spotify:playlist:37i9dQZEVXbKypXHVwk1f0',
              'PY': 'spotify:playlist:37i9dQZEVXbNOUPGj7tW6T',
              'PE': 'spotify:playlist:37i9dQZEVXbJfdy5b0KP7W',
              'UY': 'spotify:playlist:37i9dQZEVXbMJJi3wgRbAy'
              }

viral_charts = {
                'AR': 'spotify:playlist:37i9dQZEVXbJajpaXyaKll',
                'BO': 'spotify:playlist:37i9dQZEVXbMTKZuy8ORFV',
                'BR': 'spotify:playlist:37i9dQZEVXbMOkSwG072hV',
                'CL': 'spotify:playlist:37i9dQZEVXbJs8e2vk15a8',
                'CO': 'spotify:playlist:37i9dQZEVXbKrooeK9WSFF',
                'CR': 'spotify:playlist:37i9dQZEVXbKOefHPXPMyf',
                'DO': 'spotify:playlist:37i9dQZEVXbJWZV7aRNQck',
                'EC': 'spotify:playlist:37i9dQZEVXbJpRQ294oZ9N',
                'SV': 'spotify:playlist:37i9dQZEVXbLo3yC8XJf1e',
                'GT': 'spotify:playlist:37i9dQZEVXbNF1heNYHDnE',
                'HN': 'spotify:playlist:37i9dQZEVXbNpKdqfZ9Upp',
                'MX': 'spotify:playlist:37i9dQZEVXbO3qyFxbkOE1',
                'NI': 'spotify:playlist:37i9dQZEVXbKgCVIE0PTOD',
                'PA': 'spotify:playlist:37i9dQZEVXbMIO7B1pcKUy',
                'PY': 'spotify:playlist:37i9dQZEVXbNxY4E5g33Gy',
                'PE': 'spotify:playlist:37i9dQZEVXbN7gfhgaomhA',
                'UY': 'spotify:playlist:37i9dQZEVXbM1qaaFAyPLz'
                }

countries = ['AR','BO','BR','CL','CO','CR','CU','DO','EC','SV','GF','GP',
             'GT','HT','HN','MQ','MX','NI','PA','PY','PE','PR','BL','MF','UY','VE']

def get_artists(content):
    for item in content['items']:
        song = []
        for value in item['track']['artists']:
            song.append(value['name'])
        artists.append(song)
    
    return artists
    

def get_artists_from_releases(country_code):
    
    """
    Returns artists that are featured in the new releases section for a given country.
    """
    
    artists = []
    releases = sp.new_releases(country_code, limit=50)
    
    for item in content['items']:
        song = []
        for value in item['track']['artists']:
            song.append(value['name'])
        artists.append(song)
    
    return artists


def get_artists_from_playlist(playlist_uri):
    
    """
    Returns artists in order of where their songs appear in the playlist.
    """
    
    artists = []
    content = sp.playlist_items(playlist_uri)
    
    for item in content['items']:
        song = []
        for value in item['track']['artists']:
            song.append(value['name'])
        artists.append(song)
    
    return artists



def write_csv(artists, file_name):
    
    with open(file_name, 'w+') as csvfile:
        csv_writer = csv.writer(csvfile)
        for group in artists:
            csv_writer.writerow(group)
            


for country, uri in top_charts.items(): 
    file_name = 'spotify-top-charts-{}.csv'.format(country)     
    artists = get_artists_from_playlist(uri)
    write_csv(artists, file_name)
        

for country, uri in viral_charts.items():  
    file_name = 'spotify-viral-charts-{}.csv'.format(country)    
    artists = get_artists_from_playlist(uri)
    write_csv(artists, file_name)
    

for country in countries:
    file_name = 'spotify-new-releases-{}.csv'.format(country)
    artists = get_artists_from_playlist(uri)
    write_csv(artists, file_name)
    
    