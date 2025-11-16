from django.shortcuts import render
from django import forms
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = ResourceWarning(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            return render(request, "success.html", {"name": name})
        else:
            form = RegistrationForm()
        return render(request, "registrationpage.html", {"form":form})