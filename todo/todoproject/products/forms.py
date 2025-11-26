# from django import forms
# from .models import Customer
# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['email', 'password']


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price']