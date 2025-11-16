from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            return render(request, "success.html", {"name": name})
        else:
            return render(request, "registrationpage.html", {"form": form})

    form = RegistrationForm()
    return render(request, "registrationpage.html", {"form": form})
