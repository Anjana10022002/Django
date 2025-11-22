from django import forms
from .models import student_record

class studentform(forms.ModelForm):
    class Meta:
        model = student_record
        fields = '__all__'