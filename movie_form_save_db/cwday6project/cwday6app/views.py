from django.shortcuts import render
from .forms import MovieForm
from .models import Movie

def movie_data(request):
    message = ""
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            mov = Movie()
            mov.movie_name = form.cleaned_data["movie_name"]
            mov.release_year = form.cleaned_data["release_year"]
            mov.save()
            return render(request, 'success.html', {'movie': mov})
    else:
        form = MovieForm()
    return render(request, 'movie_data.html', {'form': form})
