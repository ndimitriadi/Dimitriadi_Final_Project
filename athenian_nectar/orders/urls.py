from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:exp_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/checkout/', views.checkout, name='checkout'),
]