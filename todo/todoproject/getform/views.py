from django.shortcuts import render
def greeting(request):
    if request.method == 'POST':
     email = request.POST.get('email')
     return render(request,'form-data.html',{
         'formData':request.POST,
         'email': email
     })
    return render(request,'index.html')