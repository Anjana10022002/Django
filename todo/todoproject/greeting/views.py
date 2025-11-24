# # from django.http import HttpResponse
# # def greeting(request):
# #     return HttpResponse('<h1>Hello world!</h1>')

# # from django.shortcuts import render
# # def greeting(request):
# #     return render(request,'index.html')

# from django.shortcuts import render
# def greeting(request):
#     count = 23
#     return render(request,'index.html',{'count':count})

# from django.shortcuts import render
# def greeting(request):
#     if request.method == 'POST':
#      email = request.POST.get('email')
#      return render(request,'form-data.html',{
#          'formData':request.POST,
#          'email': email
#      })
#     return render(request,'index.html')

# from django.shortcuts import render
# from .forms import LoginForm
# def greeting(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return render(request,'form-data.html',{
#                 'email': form['email'].value
#             })
#     return render(request,'index.html')

# from django.http import HttpResponse
# from .models import Customer
# def greeting(request):
#     cust = Customer()
#     cust.email = 'user2@mashupstack.com'
#     cust.password = 'hello123'
#     cust.save()
#     return HttpResponse('Db table row created')

# from django.shortcuts import render
# from .forms import LoginForm
# from .models import Customer
# def greeting(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cust = Customer()
#             cust.email = form.cleaned_data['email']
#             cust.password = form.cleaned_data['password']
#             cust.save()
#             return render(request,'form-data.html',{
#                  'message': 'Data saved to db'
#             })
#     else:
#         form = LoginForm()
#     return render(request,'index.html',{'form':form})

# from django.shortcuts import render
# from .forms import LoginModelForm
# def greeting(request):
#     if request.method == 'POST':
#         form = LoginModelForm(request.POST)
#         if form.is_valid():
#             cust = form.save()
#             return render(request,'form-data.html',{
#                 'message': 'Data saved to db'            })
#     else:
#         form = LoginModelForm()
#     return render(request,'index.html',{'form':form})

# from django.shortcuts import render
# from .forms import LoginModelForm
# from .models import Customer
# def greeting(request):
#     if request.method == 'POST':
#         form = LoginModelForm(request.POST)
#         if form.is_valid():
#             cust = form.save()
#             return render(request,'form-data.html',{
#                 'message': 'Data saved to db',
#                 'customer': cust
#             })
#     else:
#         form = LoginModelForm()
#     return render(request,'index.html',{'form':form})

# def greeting(request):
#     data = Customer.objects.all()
#     return render(request, 'index.html', {'data': data})

# from django.shortcuts import render
# from .forms import LoginModelForm

# def greeting(request):
#     if request.method == 'POST':
#         form = LoginModelForm(request.POST)
#         if form.is_valid():
#             cust = form.save()
#             return render(request,'form-data.html',{
#                 'message': 'Data saved to db',
#                 'customer': cust
#             })
#     else:
#         form = LoginModelForm()
#     return render(request,'index.html',{'form':form})

# def aboutUs(request):
#     return render(request,'about-us.html')

from django.http import HttpResponse
from django.shortcuts import render

def pagevisit(request):
    # Get the current count from the session, or set it to 0 if it doesn't exist
    count = request.session.get('page_count', 0)
    # Increment the count
    count += 1
    # Store the updated count in the session
    request.session['page_count'] = count
    # Render the template with the count variable
    return render(request,'pagevisit.html', {'count': count})


def aboutUs(request):
    return render(request,'aboutus.html')






from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
 
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('createproduct')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})



from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})