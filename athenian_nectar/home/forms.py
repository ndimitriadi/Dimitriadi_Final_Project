from django import forms
from django.core.exceptions import ValidationError

class contact_form(forms.Form):
    first_name = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-area', 
            'placeholder': 'First name',
            'aria-label': 'First name'
        })
    )
    
    last_name = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-area', 
            'placeholder': 'Last name',
            'aria-label': 'Last name'
        })
    )
    
    email = forms.EmailField(
        max_length=40,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'row form-area', 
            'placeholder': 'Your email',
            'aria-label': 'Your email address'
        })
    )
    
    subject = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'row form-area', 
            'placeholder': 'Subject',
            'aria-label': 'Message subject'
        })
    )
    
    message = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'row form-area', 
            'placeholder': 'How can we help?',
            'rows': 7,
            'aria-label': 'Your message'
        })
    )