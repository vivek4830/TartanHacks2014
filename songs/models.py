from django.db import models
from django.forms import ModelForm

import re, urllib2, urlparse
from django.contrib.auth.models import User

class YTVid(object):
    def __init__(self, url):
        self.url = url
        self.id = self.ytid(url)
        self.length = self.getDuration(url)
        self.title = self.getName(url)

    def ytid(self, url):
        """Get YouTube's video ID for the specified video"""
        return urlparse.parse_qs(urlparse.urlparse(url).query)["v"][0]

    def extractTime(self, s):
        rexp = r"<yt:duration seconds='(\d+)'/>"
        m = re.search(rexp, s)
        if m: return m.group(1)

    def extractName(self, s):
        rexp = "<title>(.+)</title>"
        m = re.search(rexp, s)
        if m: return m.group(1)
        
    def ytXML(self, url):
        dataURL = r"https://gdata.youtube.com/feeds/api/videos/{}?v=2"
        return urllib2.urlopen(dataURL.format(self.ytid(url))).read()
        
    def getDuration(self, url):
        """Return the duration of a YouTube video in seconds"""
        result = self.extractTime(self.ytXML(url))
        if result: return int(result)
        else: return -1

    def getName(self, url):
        """Return the title of a YouTube video. WARNING: this function sucks"""
        result = self.extractName(self.ytXML(url))
        return result if result else "HELLO I HAD AN OUCHIE IN YTVid.PY"

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