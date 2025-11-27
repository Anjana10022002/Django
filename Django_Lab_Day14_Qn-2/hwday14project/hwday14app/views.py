from django.shortcuts import render, redirect
from .forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ProductForm()
        return render(request, 'create.html', {'form':form})