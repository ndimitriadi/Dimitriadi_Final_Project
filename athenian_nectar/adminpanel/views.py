from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from experiences.models import Experience, Category, Subcategory
from home.models import Testimonial
from .forms import ExperienceForm, CategoryForm, SubcategoryForm, TestimonialForm, CustomUserForm
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

#experience
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

    return render(request, 'adminpanel/add_experiences.html', context)

@user_passes_test(check_admin, login_url='login') 
def delete_experience(request, exp_id):
    if request.method == 'POST':
        try:
            experience_to_delete = Experience.objects.get(id=exp_id)
            experience_to_delete.delete()
        except Experience.DoesNotExist:
            pass
            
    return redirect('add_experience')

#category
@user_passes_test(check_admin, login_url='login') 
def add_category(request):
    if request.method == 'POST':
        cat_id = request.POST.get('category_id')
        
        if cat_id:
            try:
                category_to_update = Category.objects.get(id=cat_id)
                form = CategoryForm(request.POST, request.FILES, instance=category_to_update)
            except Category.DoesNotExist:
                form = CategoryForm(request.POST, request.FILES)
        else:

            form = CategoryForm(request.POST, request.FILES) 
            
        if form.is_valid():
            form.save() 
            return redirect('add_category') 
    
    else:
        form = CategoryForm()
        
    all_categories = Category.objects.all().order_by('-id') 
        
    context = {
        'form': form,
        'categories': all_categories, 
    }
    return render(request, 'adminpanel/add_category.html', context) 


@user_passes_test(check_admin, login_url='login') 
def delete_category(request, cat_id):
    if request.method == 'POST':
        try:
            category_to_delete = Category.objects.get(id=cat_id)
            category_to_delete.delete()
        except Category.DoesNotExist:
            pass 
            
    return redirect('add_category')

#subcategory
@user_passes_test(check_admin, login_url='login') 
def add_subcategory(request):
    if request.method == 'POST':
        sub_id = request.POST.get('subcategory_id')
        
        if sub_id:
            try:
                sub_to_update = Subcategory.objects.get(id=sub_id)
                form = SubcategoryForm(request.POST, request.FILES, instance=sub_to_update)
            except Subcategory.DoesNotExist:
                form = SubcategoryForm(request.POST, request.FILES)
        else:
            form = SubcategoryForm(request.POST, request.FILES) 
            
        if form.is_valid():
            form.save() 
            return redirect('add_subcategory') 
    else:
        form = SubcategoryForm()
        
    all_subcategories = Subcategory.objects.select_related('category').all().order_by('-id') 
        
    context = {
        'form': form,
        'subcategories': all_subcategories, 
    }
    return render(request, 'adminpanel/add_subcategory.html', context) 

@user_passes_test(check_admin, login_url='login') 
def delete_subcategory(request, sub_id):
    if request.method == 'POST':
        try:
            sub_to_delete = Subcategory.objects.get(id=sub_id)
            sub_to_delete.delete()
        except Subcategory.DoesNotExist:
            pass 
            
    return redirect('add_subcategory')


#testimonial
@user_passes_test(check_admin, login_url='login') 
def add_testimonial(request):
    if request.method == 'POST':
        t_id = request.POST.get('testimonial_id')
        
        if t_id:
            try:
                test_to_update = Testimonial.objects.get(id=t_id)
                form = TestimonialForm(request.POST, request.FILES, instance=test_to_update)
            except Testimonial.DoesNotExist:
                form = TestimonialForm(request.POST, request.FILES)
        else:
            form = TestimonialForm(request.POST, request.FILES) 
            
        if form.is_valid():
            form.save() 
            return redirect('add_testimonial') 
    else:
        form = TestimonialForm()
        
    all_testimonials = Testimonial.objects.all().order_by('-id') 
        
    context = {
        'form': form,
        'testimonials': all_testimonials, 
    }
    return render(request, 'adminpanel/add_testimonial.html', context) 

@user_passes_test(check_admin, login_url='login') 
def delete_testimonial(request, t_id):
    if request.method == 'POST':
        try:
            test_to_delete = Testimonial.objects.get(id=t_id)
            test_to_delete.delete()
        except Testimonial.DoesNotExist:
            pass 
            
    return redirect('add_testimonial')

#users
@user_passes_test(check_admin, login_url='login') 
def add_user(request):
    edit_id = None 
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        edit_id = user_id #savign id if there are errors
        
        if user_id:
            try:
                user_to_update = User.objects.get(id=user_id)
                form = CustomUserForm(request.POST, instance=user_to_update)
            except User.DoesNotExist:
                form = CustomUserForm(request.POST)
        else:
            form = CustomUserForm(request.POST) 
            
        if form.is_valid():
            form.save() 
            return redirect('add_user') 
    else:
        form = CustomUserForm()
        
    all_users = User.objects.all().order_by('-date_joined') 
        
    context = {
        'form': form,
        'users': all_users, 
        'edit_id': edit_id,
    }
    return render(request, 'adminpanel/add_user.html', context)

@user_passes_test(check_admin, login_url='login') 
def delete_user(request, user_id):
    if request.method == 'POST':
        try:
            user_to_delete = User.objects.get(id=user_id)
            #preventing logged in user from deleting themselves
            if user_to_delete.id != request.user.id:
                user_to_delete.delete()
        except User.DoesNotExist:
            pass 
            
    return redirect('add_user')