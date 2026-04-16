from django.shortcuts import render
from .models import Experience, Category, Subcategory

# Create your views here.

def discover(request):
    all_items = Experience.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    durations = Experience.objects.exclude(duration__isnull=True).values_list('duration', flat=True).distinct().order_by('duration')

    context = {
        'items': all_items,
        'categories': categories,
        'subcategories': subcategories,
        'durations': durations,
    }

    return render(request, 'experiences/discover.html', context)