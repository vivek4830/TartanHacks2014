
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader as templateLoader, RequestContext
from django.shortcuts import render

from songs.models import Song, YTVid
from songs.forms import SongForm

def mainIndex(request):
    """List all songs and their info"""
    song_list = Song.objects.all()
    song_list = Song.objects.all()[:5]
    template = templateLoader.get_template("songs/index.html")
    context = {"song_list" : song_list}
    return render(request, "songs/index.html", context)

def index(request):
    """Play a YT video"""
    one_song = Song.objects.all()[0]
    Y = YTVid(one_song.songUrl) # remember, this is just Youtube vids now
    contextVars = {
        "video_title" : Y.title,
        "duration"    : Y.length,
        "video_id"    : Y.id,
    }
    return render(request, "songs/autoplay.html", contextVars)

def playlist(request, playlist_id, playlist_index):
    """Process a playlist, starting with playlist_index"""
    song_list = Song.objects.filter(playlistID__exact=playlist_id,
                                    playlistPosition__exact=int(playlist_index))
    if (len(song_list) != 1):
        print "Bad playlist ID or playlist index"
        exit(1)
    
    Y = YTVid(song_list[0].songUrl)
    contextVars = {
        "video_title" : Y.title,
        "video_id"    : Y.id,
    }
    return render(request, "songs/autoplay.html", contextVars)

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