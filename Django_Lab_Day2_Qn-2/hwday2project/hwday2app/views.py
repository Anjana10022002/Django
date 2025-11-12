from django.shortcuts import render

def gallerypage(request):
    return render(request, 'gallerypage.html')

def contactpage(request):
    return render(request, 'contactpage.html')