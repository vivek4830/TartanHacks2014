from django.contrib import admin
from songs.models import Song, Playlist

# Register your models here.

class SongAdmin(admin.ModelAdmin):
	list_display = ('songName', 'songUrl', 'playlistID', 'playlistPosition')

class PlaylistAdmin(admin.ModelAdmin):
	list_display = ('playlistID', 'playlistName')

admin.site.register(Song, SongAdmin)
admin.site.register(Playlist, PlaylistAdmin)