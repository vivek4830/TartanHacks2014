
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader as templateLoader, RequestContext
from django.shortcuts import render

from songs.models import Song

def index(request):
    """List all songs and their info"""
    song_list = Song.objects.all()
    template = templateLoader.get_template("songs/index.html")
    context = {"song_list" : song_list}
    return render(request, "songs/index.html", context)

def playlist(request, playlist_id):
    """List all songs in the playlist. Takes playlist ID as second arg"""
    song_list = Song.objects.filter(playlistID__exact=playlist_id)
    template = templateLoader.get_template("songs/playlistList.html")
    contextVars = {
        "playlistID" : playlist_id,
        "song_list"  : song_list
    }
    return render(request, "songs/playlistList.html", contextVars)