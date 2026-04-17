from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm, UserUpdateForm, CustomPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from experiences.models import Experience
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:  
            u_form = UserUpdateForm(request.POST, instance=request.user)          
            if u_form.is_valid():
                u_form.save()
                messages.success(request, 'Your profile has been successfully updated!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Profile update failed. Please check the errors below.')

        elif 'change_password' in request.POST:
            p_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            
            if p_form.is_valid():
                p_form.save()
                update_session_auth_hash(request, p_form.user) 
                messages.success(request, 'Your password was successfully changed!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Password change failed. Please check the errors below.')

    profile, created = Profile.objects.get_or_create(user=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'recently_viewed': [], 
        'ratings': [],
        'purchases': [],     
        'favorites': profile.favorites.all(),
    }
    
    return render(request, 'users/dashboard.html', context)

def favorite(request, item_id):
    if request.method == 'POST':
        experience = get_object_or_404(Experience, id=item_id) #if the object doesnt exist, it will be handled with a 404
        profile = request.user.profile
        
        if experience in profile.favorites.all():
            profile.favorites.remove(experience)
            is_favorited = False
        else:
            profile.favorites.add(experience)
            is_favorited = True
            
        return JsonResponse({'is_favorited': is_favorited})