from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from experiences.models import Experience
from .forms import ExperienceForm
# Create your views here.

#admin panel
def check_admin(user):
    return user.is_superuser # or user.is_staff if you want to be stricter

@user_passes_test(check_admin, login_url='login') 
def admin_panel(request):
    total_users = User.objects.count()
    all_experiences = Experience.objects.all()

    context = {
        'total_users': total_users,
        'experiences': all_experiences,
    }
    
    return render(request, 'adminpanel/admin_panel.html', context)

#add experience
def add_experience(request):
 
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('add_experience') 
    
    else:
        form = ExperienceForm()
        
    context = {
        'form': form,
        'action': 'Add New Experience'
    }
    return render(request, 'adminpanel/add_experiences', context)