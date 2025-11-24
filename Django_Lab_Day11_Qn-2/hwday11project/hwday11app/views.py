from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createproduct')
    else:
        form = UserCreationForm()
    return render(request, "signup.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
