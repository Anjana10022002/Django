from django import forms
from hwday11app import book_club
class UserCreationForm(forms.modelForm):
    class meta:
        model = book_club
        field = '__all__'
