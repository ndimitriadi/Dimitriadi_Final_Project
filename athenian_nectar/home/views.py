from django.shortcuts import render
from .forms import contact_form
from .models import Testimonial

# Create your views here.
def home(request):
    all_testimonials = Testimonial.objects.all() 
    return render(request, 'home/index.html', {'testimonials': all_testimonials})

def about(request):
    return render(request, 'home/about_us.html')

def contact(request):
    form = contact_form()
    details = {'form': form}
    return render(request, 'home/contact_us.html', details)