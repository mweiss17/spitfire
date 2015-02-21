from django import forms

class search_spitfire_form(forms.Form):
	search_query = forms.CharField(label='Search for Music', max_length=140)
