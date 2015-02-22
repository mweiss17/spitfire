from django import forms

class search_spitfire_form(forms.Form):
	#search_query = forms.CharField(label='', max_length=140, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Search'}))
	search_query = forms.CharField(label='', max_length=140)
