from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20, 
        min_length=4, 
    )

    email = forms.EmailField(
        max_length=35, 
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email'] 

    #ensures lowercase usernames
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.help_text = ''

        for field_name, field in self.fields.items():
            if 'password' in field_name.lower():
                field.widget.attrs['maxlength'] = '30'


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=20, min_length=4)
    email = forms.EmailField(max_length=35, required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removes that giant list of password rules
        for field in self.fields.values():
            field.help_text = ''
        
        # Sets the physical character limit in the browser
        for field_name, field in self.fields.items():
            field.widget.attrs['maxlength'] = '30'