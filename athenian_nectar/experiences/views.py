from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Experience, Category, Subcategory, Review
from django.contrib import messages
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
            return redirect(f"{reverse('experience_detail', args=[experience.id])}")

        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.experience = experience
            new_review.user = request.user
            new_review.save()
            
            return redirect(f"{reverse('experience_detail', args=[experience.id])}")
    else:
        form = ReviewForm()

    #recommendations based on same category
    recommended = list(Experience.objects.filter(
        category=experience.category
    ).exclude(
        id=experience.id
    ).order_by('?')[:3])
    # order_by('?') shuffles 
    #[:3] grabs only 3

    #if there are less than 3 experiences matching the category
    if len(recommended) < 3:
        empty_spots = 3 - len(recommended)
        
        #ids we already have so we don't accidentally duplicate them
        existing_ids = [rec.id for rec in recommended]
        existing_ids.append(experience.id)
        
        # Grab random experiences to fill the holes
        fillers = Experience.objects.exclude(
            id__in=existing_ids
        ).order_by('?')[:empty_spots]
        
        recommended.extend(fillers)
        
    context = {
        'experience': experience,
        'reviews': reviews,
        'form': form,
        'has_reviewed': has_reviewed,
        'recommended_experiences': recommended,
    }
    return render(request, 'experiences/experience_detail.html', context)


@require_POST
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    exp_id = review.experience.id 
    
    review.delete()
    return redirect(f"{reverse('experience_detail', args=[exp_id])}")