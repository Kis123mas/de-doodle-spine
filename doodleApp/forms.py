from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent border border-white'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-transparent border border-white'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-transparent border border-white'}),
            'subject': forms.TextInput(attrs={'class': 'form-control bg-transparent border border-white'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-transparent border border-white', 'style': 'height:160px;'}),
        }
