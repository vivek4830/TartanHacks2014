from django.db import models
from django.forms import ModelForm

class Playlist(models.Model):
	playlistID = models.IntegerField(default = 1)
	playlistName = models.CharField(max_length = 200)

# Create your models here.
class Song(models.Model):
	playlist = models.ForeignKey(Playlist, default = 1)
	songName = models.CharField(max_length = 200)
	songUrl = models.CharField(max_length = 250)
	playlistID = models.IntegerField(default = 1)
	playlistPosition = models.IntegerField(default = 1)