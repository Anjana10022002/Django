# from django import forms
# class LoginForm(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField()
 
from django import forms
class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,min_length=10)
    password = forms.CharField(max_length=50,min_length=6)