from django import forms
from cwday11app import User_details

class Details_form(forms.ModelForm):
    class Meta:
        model = User_details
        fields = '__all__'
