from django import forms
from experiences.models import Experience, Category, Subcategory

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'subcategory', 'description', 'image', 'price', 'duration', 'rating', 'total_reviews'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '40'}),
            'category': forms.Select(attrs={'class': 'form-select'}), 
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'maxlength': '3000'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'value': '5.0'}),
            'total_reviews': forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
        }