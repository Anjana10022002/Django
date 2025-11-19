from django.shortcuts import render
from .models import Customer
from .forms import cust_details_form

def cus_deatils(request):
    if request.method == 'POST':
        form = cust_details_form(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request, "user_details.html",
                          {'message':'User data saved to DB'})
        else:
            form = cust_details_form()
        return render(request, 'index.html',{'form':form})
