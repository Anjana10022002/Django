from django import forms
from .models import Movie

class MovieForm(forms.Form):
    movie_name = forms.CharField(max_length=100, min_length=5)
    release_year = forms.IntegerField()