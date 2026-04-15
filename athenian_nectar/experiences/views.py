from django.shortcuts import render
from .models import Experience

# Create your views here.

def discover(request):
    # Fetch all items from the database
    all_items = Experience.objects.all()
    
    # Send them to the template
    context = {'items': all_items}
    return render(request, 'experiences/discover.html', context)