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