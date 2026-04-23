from django.db import models
from django.conf import settings
from experiences.models import Experience

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # We can track order status (e.g., Pending, Paid, Cancelled)
    status = models.CharField(max_length=20, default='Paid')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # We use SET_NULL so if you ever delete an Experience from the site, 
    # it doesn't delete the user's past purchase history!
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.experience.title} (Order #{self.order.id})"