from django.shortcuts import render
from spitfire.forms import *

def index(request):
	context = {}
	if request.method == "POST":
		search_form = search_spitfire_form(request.POST)
		if search_form.is_valid():
			query = search_form.cleaned_data["search_query"]
			context.update({"query":query})
			return render(request, 'other.html', context)	
	search_form = search_spitfire_form()	
	context.update({"search_form":search_form})
	return render(request, 'index.html', context)

def other(request):
	context = {}
	return render(request, 'other.html', context)

