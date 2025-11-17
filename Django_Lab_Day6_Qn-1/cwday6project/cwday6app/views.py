from django.shortcuts import render
from .forms import MovieForm

def movie_data(request):
    if request.method == 'POST':
        form = movie_data(request.POST)
        if form.is_valid():
            
            movie = form.save()       
            return render(request, 'success.html', {'movie': movie})
    else:
        form = MovieForm()
    return render(request, 'movie_data.html', {'form': form})