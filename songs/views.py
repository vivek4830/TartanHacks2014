
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader as templateLoader, RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse

from songs.models import Song, YTVid
from songs.forms import SongForm, UserForm

def mainIndex(request):
    """List all songs and their info"""
    song_list = Song.objects.all()
    song_list = Song.objects.all()[:5]
    template = templateLoader.get_template("songs/index.html")
    context = {"song_list" : song_list}
    return render(request, "songs/index.html", context)

def index(request):
    """Play a YT video"""
    one_song = Song.objects.all()[3]
    Y = YTVid(one_song.songUrl) # remember, this is just Youtube vids now
    contextVars = {
        "video_title" : Y.title,
        "duration"    : Y.length,
        "video_id"    : Y.id,
    }
    return render(request, "songs/autoplay.html", contextVars)

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

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'songs/register.html',
            {'user_form': user_form, 'registered': registered},
            context)