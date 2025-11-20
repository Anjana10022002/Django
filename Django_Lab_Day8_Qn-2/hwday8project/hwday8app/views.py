from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contascus(request):
    return render(request, 'contascus.html')

def aboutus(request):
    return render(request, 'aboutus.html')