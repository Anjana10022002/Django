from django import forms
class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=50, min_length=5)
    