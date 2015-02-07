from django import forms
from django.contrib.auth.models import User
from songs.models import UserProfile

class SongForm(forms.Form):
	songName = forms.CharField()
	songUrl = forms.CharField()
	playlistID = forms.IntegerField()
	playlistPosition = forms.IntegerField()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')