from django import forms

class SongForm(forms.Form):
	songName = forms.CharField()
	songUrl = forms.CharField()
	playlistID = forms.IntegerField()
	playlistPosition = forms.IntegerField()

class PlaylistForm(forms.Form):
	