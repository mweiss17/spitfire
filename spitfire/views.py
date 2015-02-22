from django.shortcuts import render
from spitfire.forms import *
from search_youtube import youtube_search

def index(request):
	context = {}
	if request.method == "POST":
		search_form = search_spitfire_form(request.POST)
		if search_form.is_valid():
			query = search_form.cleaned_data["search_query"]
			results =  youtube_search(query)
			result_codes = []
			track_titles = []
			for result in results:
				result_codes.append(result[-12:-1])
				track_titles.append(result[:-14])
			context.update({"track_titles": track_titles, "result_codes":result_codes})
			return render(request, 'index.html', context)	

	search_form = search_spitfire_form()	
	context.update({"search_form":search_form})
	return render(request, 'index.html', context)

def other(request):
	context = {}

	return render(request, 'other.html', context)

