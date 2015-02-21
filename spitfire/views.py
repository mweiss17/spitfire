from django.shortcuts import render
from spitfire.forms import *

def index(request):
    context = {}
    #results = search_youtube(request.get['query_name_orwe'])
    search_form = search_spitfire_form(request.POST)
    context.update({"search_form":search_form})
    if search_form.is_valid(): 
	return render(request, 'valid.html', context)
    return render(request, 'index.html', context)
