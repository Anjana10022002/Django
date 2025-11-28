from django import forms
from .models import certificates

class CertificateForm(forms.ModelForm):
    class Meta:
        model = certificates
        fields = '__all__'