from django.urls import path
from . import views

urlpatterns = [
    path('', views.discover, name='discover'),
    path('experience/<int:exp_id>/', views.experience_detail, name='experience_detail'),
]