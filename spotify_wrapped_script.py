import requests
import os
from datetime import datetime


def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': 'Basic ' +  os.environ.get('SPOTIFY_CLIENTID_AND_SECRET_BASE64')}
    payload = {'grant_type': 'refresh_token', 'refresh_token': os.environ.get('SPOTIFY_REFRESH_TOKEN')}
    r = requests.post(url, headers=headers, data=payload)
    return r.json().get('access_token')

def get_my_top_25_tracks(access_token):
    url = 'https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=25'
    headers = {'Authorization': 'Bearer ' + access_token}
    r = requests.get(url, headers=headers)
    body_json = r.json()
    track_id_list = []
    for track in body_json['items']:
        track_id_list.append(track['id'])
    return track_id_list

def create_top_25_playlist(track_id_list, playlist_name, access_token):
    headers = {'Authorization': 'Bearer ' + access_token}

    create_playlist_url = 'https://api.spotify.com/v1/users/' + os.environ.get('SPOTIFY_USER_ID') + '/playlists'
    create_playlist_body = {"name": playlist_name, "public": False}
    create_playlist_response = requests.post(create_playlist_url, json=create_playlist_body, headers=headers)
    playlist_id = create_playlist_response.json().get('id')

    add_tracks_url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    track_id_list_formatted = []
    for track_id in track_id_list:
        track_id_list_formatted.append('spotify:track:' + track_id)
    add_tracks_body = {"uris": track_id_list_formatted}
    add_tracks_response = requests.post(add_tracks_url, json=add_tracks_body, headers=headers)
    if add_tracks_response.status_code == 201:
        print ('Playlist successfully created and tracks added!')
    else:
        print('Adding tracks to playlist failed. Check logs for more info.')

def getCurrentMonth():
    today = datetime.now()
    return today.strftime("%b")

def getCurrentYear():
    today = datetime.now()
    return today.year

def getPlaylistName():
    return "Peer's Top 25 - " + getCurrentMonth() + " " + str(getCurrentYear())

#calling the magic
access_token = get_access_token()
create_top_25_playlist(get_my_top_25_tracks(access_token), getPlaylistName(), access_token)