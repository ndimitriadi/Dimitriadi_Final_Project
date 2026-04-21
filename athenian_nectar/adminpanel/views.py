from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from experiences.models import Experience, Category, Subcategory
from .forms import ExperienceForm
# Create your views here.

#admin panel
def check_admin(user):
    return user.is_superuser # or user.is_staff 

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
@user_passes_test(check_admin, login_url='login') 
def add_experience(request):
    if request.method == 'POST':
        exp_id = request.POST.get('experience_id')
        
        if exp_id:
            try:
                experience_to_update = Experience.objects.get(id=exp_id)
                form = ExperienceForm(request.POST, request.FILES, instance=experience_to_update)
            except Experience.DoesNotExist:
                form = ExperienceForm(request.POST, request.FILES)
        else:
            form = ExperienceForm(request.POST, request.FILES) 
            
        if form.is_valid():
            form.save() 
            return redirect('add_experience') 
    
    else:
        form = ExperienceForm()
        
    all_experiences = Experience.objects.all().order_by('-id') 

    #subcategories correspond to categories
    category_map = {}
    all_categories = Category.objects.all()
    
    for cat in all_categories:
        subs = Subcategory.objects.filter(category=cat)
        category_map[cat.name] = [str(sub.id) for sub in subs]

    context = {
        'form': form,
        'experiences': Experience.objects.all().order_by('-id'), 
        'category_map': category_map,
    }

    return render(request, 'adminpanel/add_experiences', context)

    


@user_passes_test(check_admin, login_url='login') 
def delete_experience(request, exp_id):
    if request.method == 'POST':
        try:
            experience_to_delete = Experience.objects.get(id=exp_id)
            experience_to_delete.delete()
        except Experience.DoesNotExist:
            pass
            
    return redirect('add_experience')