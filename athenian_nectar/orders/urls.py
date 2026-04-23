from django.urls import path
from . import views

urlpatterns = [
    path('/add/<int:exp_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('/checkout/', views.checkout, name='checkout'),
    path('/update/<int:exp_id>/', views.update_cart, name='update_cart'),
    path('/remove/<int:exp_id>/', views.remove_from_cart, name='remove_from_cart'),
]