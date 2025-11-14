from django.shortcuts import render

def userform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render (request, 'user_data_form.html'),{
            'formData' : request.POST,
            'name' : name
        }
    return render(request, 'user_data_form.html')