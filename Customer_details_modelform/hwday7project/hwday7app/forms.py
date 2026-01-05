from django import forms
from .models import Customer

class cust_details_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']