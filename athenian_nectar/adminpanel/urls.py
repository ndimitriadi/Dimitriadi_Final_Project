from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'), 
    path('experience/add/', views.add_experience, name='add_experience'),
]