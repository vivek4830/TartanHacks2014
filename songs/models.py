from django.db import models

# Create your models here.

class Song(models.Model):
	songName = models.CharField(max_length = 200)
	songUrl = models.CharField(max_length = 250)