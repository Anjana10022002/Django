from django.shortcuts import render
from .models import Customer
from .forms import cust_details_form

def cus_details(request):
    if request.method == 'POST':
        form = cust_details_form(request.POST)
        if form.is_valid():
            saved = form.save()
            return render(request, "user_details.html",
                          {'message': 'User data saved to DB',
                           'customer': saved})
    else:
        form = cust_details_form()

    return render(request, "user_details.html", {'form': form})
    

def all_customers(request):
    cust = Customer.objects.all().order_by('name')
    return render(request, 'all_customers.html', {'customers': cust})


def filt_customers(request):
    cust = Customer.objects.filter(email__endswith='@example.com')
    return render(request, 'filtered_customers.html', {'customers': cust})
