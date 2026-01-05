from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

def aboutus(request):
    return render(request, 'aboutus_page.html')