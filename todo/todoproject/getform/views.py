# from django.shortcuts import render
# def greeting(request):
#     if request.method == 'POST':
#      email = request.POST.get('email')
#      return render(request,'form-data.html',{
#          'formData':request.POST,
#          'email': email
#      })
#     return render(request,'index.html')

from django.shortcuts import render
def greeting(request):
    if request.GET:
        email = request.GET.get('email')
        return render(request,'form-data.html',{
            'formData':request.GET,
            'email': email
        })
    return render(request,'index.html' )

from django.shortcuts import render
from .forms import LoginForm
def greeting(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        return render(request,'form-data.html',{
            'email': form['email'].value
        })
    return render(request,'index.html')