import sys
import os
import spotipy
import spotipy.util as util
import json
import warnings
warnings.simplefilter("ignore", UnicodeWarning)
import unicodedata

f = open("sxswscrape.txt")
data = []
setS = []
for l in f.readlines():
    s = str(l).rstrip('\n')
    #print s
    data.append(s)

def find(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        artist = track['artists'][0]['name']
        if (artist in data and artist not in setS):
              setS.append(str(track['artists'][0]['name']))
             
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Whoops, need your username!"
    print "usage: python user_playlists.py [username]"
    sys.exit()


    
token = util.prompt_for_user_token(username)
if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    boo = raw_input("Would you like to select a specific playlist? y/n ")
    if boo != 'y' and boo != 'n':
        print "Please input y or n next time. idiot."
        sys.exit()

    if boo == 'n':
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                name =  playlist['name']
                #if (name == 'feb'):          
                #print '  total tracks', playlist['tracks']['total']
                results = sp.user_playlist(username, playlist['id'],fields="tracks,next")
                tracks = results['tracks']
                find(tracks)
    else:
        chk = raw_input("Please input playlist name!\n")
        found = False
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                name =  playlist['name']
                if (name == chk):          
                    results = sp.user_playlist(username, playlist['id'],fields="tracks,next")
                    tracks = results['tracks']
                    find(tracks)
                    found = True
        if (found == False):
            print "No playlist found!!"

else:
    print "Can't get token for", username

for x in setS:
    print x
    