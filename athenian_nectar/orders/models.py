from django.db import models
from django.conf import settings
from experiences.models import Experience

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    booking_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.experience.title} on {self.booking_date} (Order #{self.order.id})"