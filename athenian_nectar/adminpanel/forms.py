from django import forms
from experiences.models import Experience, Category, Subcategory
from home.models import Testimonial
from django.contrib.auth.models import User

#experiences
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'subcategory', 'description', 'image', 'price', 'duration'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '40'}),
            'category': forms.Select(attrs={'class': 'form-select'}), 
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'maxlength': '3000'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
        }
#category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
        }

#subcategory
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
        }

#testimonials
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'quote', 'stars']

#users
class CustomUserForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('user', 'Regular User'),
        ('staff', 'Staff'),
        ('superuser', 'Superuser')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    
    # old password
    old_password = forms.CharField(
        label="Current Password",
        required=False
    )
    
    #new password
    password = forms.CharField(
        label="New Password",
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.is_superuser:
                self.fields['status'].initial = 'superuser'
            elif self.instance.is_staff:
                self.fields['status'].initial = 'staff'
            else:
                self.fields['status'].initial = 'user'


    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("password")
        
        email = cleaned_data.get("email") 
        
        if self.instance.pk: 
            #old password check (for old users)
            if new_password:
                if not old_password:
                    self.add_error('old_password', "You must provide the current password to set a new one.")
                elif not self.instance.check_password(old_password):
                    self.add_error('old_password', "The current password you entered is incorrect.")
        else: 
            #requirement fields (for new users)
            if not new_password:
                self.add_error('password', "Password required.")
                
            if not email:
                self.add_error('email', "Email address required.")
            
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        status = self.cleaned_data.get('status')
        new_password = self.cleaned_data.get('password')
        
        if status == 'superuser':
            user.is_superuser = True
            user.is_staff = True
        elif status == 'staff':
            user.is_superuser = False
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        #allows password change if the correct previous one is provided
        if new_password:
            user.set_password(new_password)

        if commit:
            user.save()
        return user