from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'), 
    path('experience/add/', views.add_experience, name='add_experience'),
    path('experience/delete/<int:exp_id>/', views.delete_experience, name='delete_experience'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/delete/<int:cat_id>/', views.delete_category, name='delete_category'),
    path('subcategory/add/', views.add_subcategory, name='add_subcategory'),
    path('subcategory/delete/<int:sub_id>/', views.delete_subcategory, name='delete_subcategory'),
]