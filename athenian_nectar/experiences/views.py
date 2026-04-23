from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Experience, Category, Subcategory
from django.contrib import messages
from .models import Experience, Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST

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
    
#reviews
def experience_detail(request, exp_id):
    experience = get_object_or_404(Experience, id=exp_id)
    reviews = experience.reviews.all().order_by('-created_at')

    recently_viewed = request.session.get('recently_viewed', [])
    if exp_id in recently_viewed:
        recently_viewed.remove(exp_id)
    recently_viewed.insert(0, exp_id)
    request.session['recently_viewed'] = recently_viewed[:4]
    
    has_reviewed = False
    if request.user.is_authenticated:
        has_reviewed = Review.objects.filter(user=request.user, experience=experience).exists()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        if has_reviewed:
            messages.error(request, "You have already reviewed this experience.")
            return redirect(f"{reverse('experience_detail', args=[experience.id])}#reviews-section")

        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.experience = experience
            new_review.user = request.user
            new_review.save()
            
            return redirect(f"{reverse('experience_detail', args=[experience.id])}#about")
    else:
        form = ReviewForm()
        
    context = {
        'experience': experience,
        'reviews': reviews,
        'form': form,
        'has_reviewed': has_reviewed,
    }
    return render(request, 'experiences/experience_detail.html', context)


@require_POST
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    exp_id = review.experience.id 
    
    review.delete()
    return redirect(f"{reverse('experience_detail', args=[exp_id])}#about")