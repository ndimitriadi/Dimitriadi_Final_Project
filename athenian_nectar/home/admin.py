from django.contrib import admin
from .models import Testimonial

# This "decorator" attaches your custom settings to the model
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # 1. Choose which columns show up in the main list
    list_display = ('name', 'role', 'stars')
    
    # 2. Add a search bar that searches by name or quote
    search_fields = ('name', 'quote')
    
    # 3. Add a filter box on the right side to sort by star rating
    list_filter = ('stars',)
    
    # 4. (Optional) Make fields editable directly from the list page!
    list_editable = ('stars',)