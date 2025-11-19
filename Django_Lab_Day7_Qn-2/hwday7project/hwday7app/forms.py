from django import forms
from .models import Customer

class cust_details_form(forms.Modelform):
    class Meta:
        model = Customer
        feilds = ['name', 'email']
