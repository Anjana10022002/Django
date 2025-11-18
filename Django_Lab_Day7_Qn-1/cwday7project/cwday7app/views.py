from django.shortcuts import render
from .forms import libraryForm
from .models import Library

def book(request):
    if request.method == 'POST':
        form = libraryForm(request.POST)
        if form.is_valid():
            books = form.save()
            return render(request, 'saved_books.html',
                          {'message': 'Data saved to db', 
                          'book_data':books})
    else:
        form = libraryForm()
    return render(request, 'index.html', {'form':form})
def view_books(request):
    books = Library.objects.all()
    return render(request, 'saved_books.html', {'books': books})