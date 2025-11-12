from django.shortcuts import render

def gallery(request):
    return render(request, 'gallerypage.html')

def contact(request):
    return render(request, 'contactme.html')
