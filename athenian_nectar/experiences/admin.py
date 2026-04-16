from django.contrib import admin
from django import forms
from .models import Category, Subcategory, Experience

# Register your models here.
class ExperienceAdminForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'duration': forms.NumberInput(attrs={'step': '0.5'})
        }
class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Experience, ExperienceAdmin)