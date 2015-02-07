from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the songs index.")

def playlist(request, playlist_id):
	return HttpResponse("You're looking at the songs in playlist %s." % playlist_id)