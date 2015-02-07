
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader as templateLoader, RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse

from songs.models import Song
from songs.forms import SongForm

def index(request):
    """List all songs and their info"""
    song_list = Song.objects.all()
    song_list = Song.objects.all()[:5]
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

def addSong(request):
	if request.method == 'POST':
		form = SongForm(request.POST)
		if form.is_valid():
			# Process form data from form.cleaned_data
			currentSong = Song()
			currentSong.songName = form.cleaned_data['songName']
			currentSong.songUrl = form.cleaned_data['songUrl']
			currentSong.playlistID = form.cleaned_data['playlistID']
			currentSong.playlistPosition = form.cleaned_data['playlistPosition']
			currentSong.save()
			return HttpResponseRedirect("/songs/")
	else:
		form = SongForm()

	return render(request, 'songs/addSong.html', {'form': form})