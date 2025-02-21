from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']
        widgets = {
            'request_type': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
