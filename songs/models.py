from django.db import models

# Create your models here.
class Song(models.Model):
	songName = models.CharField(max_length = 200)
	songUrl = models.CharField(max_length = 250)
	playlistID = models.IntegerField(default = -1)
	playlistPosition = models.IntegerField(default = -1)
    BUTTSXE = models.CharField(max_length = 69)<<<<<<< HEAD
    BUTTSXE = models.CharField(max_length = 69)
=======
>>>>>>> origin/master
