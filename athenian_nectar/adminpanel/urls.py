from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'), 
    path('experience/add/', views.add_experience, name='add_experience'),
    path('experience/delete/<int:exp_id>/', views.delete_experience, name='delete_experience'),
]