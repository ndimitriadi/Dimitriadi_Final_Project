from django import forms
from experiences.models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'subcategory', 'description', 'image', 'price', 'duration', 'rating', 'total_reviews'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}), 
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'value': '5.0'}),
            'total_reviews': forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}),
        }