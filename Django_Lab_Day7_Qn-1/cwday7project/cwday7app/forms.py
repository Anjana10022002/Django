from django import forms
from .models import Library

class libraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'