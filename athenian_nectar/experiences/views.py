from django.shortcuts import render, get_object_or_404
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
    
def experience_detail(request, exp_id):
    # Go to the database and get the experience where the ID matches the URL
    experience = get_object_or_404(Experience, id=exp_id)
    
    context = {
        'experience': experience,
    }
    return render(request, 'experiences/experience_detail.html', context)