import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

#setting the client ID and secret to app assignment from API
cid ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #!GET 
secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #!GET

#Set env variables for client ID, clinet secret, and redirect URL
os.environ['SPOTIPY_CLIENT_ID']= cid
os.environ['SPOTIPY_CLIENT_SECRET']= secret
os.environ['SPOTIPY_REDIRECT_URI']= 'http:/localhost:8888/callback'

#Auth flow via spotify documentation. User provides login info on first runtime 
def get_user_creds():
    username= "" #!GET
    client_credentials_manager= SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp= spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    scope = 'user-top-read'
    token= util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        return("Thanks for logging in", username)
        return token
    else:
        return("Can't get token for", username)

#Query last 6 months of users song choices and return top 50
def get_six_months(token, username):
    if token:
        sp = spotipy.Spotify(auth=token)
        topFifty = sp.current_user_top_tracks(limit=50,offset=0,time_range='medium_term')
        for song in range(50):
            list = []
            list.append(topFifty)
            with open('top50_data.json', 'w', encoding='utf-8') as f:
                json.dump(list, f, ensure_ascii=False, indent=4)
                return("Downloaded top 50 listens for", username)
        else:
            return("Can't get token for", username)