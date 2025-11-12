# from django.http import HttpResponse
# def greeting(request):
#     return HttpResponse('<h1>Hello world!</h1>')

# from django.shortcuts import render
# def greeting(request):
#     return render(request,'index.html')

from django.shortcuts import render
def greeting(request):
    count = 23
    return render(request,'index.html',{'count':count})