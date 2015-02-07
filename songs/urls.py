from django.conf.urls import patterns, url

from songs import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'addSong/$', views.addSong, name='addSong'),
	url(r'register/$', views.register, name = 'register'),
	url(r'^(?P<playlist_id>\d+)/$', views.playlist, name = 'playlist'),
)