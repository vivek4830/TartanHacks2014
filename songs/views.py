
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader as templateLoader, RequestContext
from django.shortcuts import render

from songs.models import Song

def index(request):
    """List all songs and their info"""
    song_list = Song.objects.all()[:5]
    template = templateLoader.get_template("songs/index.html")
    context = {"song_list" : song_list}
    return render(request, "songs/index.html", context)

def playlist(request, playlist_id):
	return HttpResponse("You're looking at the songs in playlist %s." % playlist_id)