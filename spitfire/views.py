from django.shortcuts import render
from search_youtube.py import youtube_search

def index(request):
    context = {}
    results = search_youtube(request.get['query_name_orwe'])
    
    return render(request, 'index.html', context)
