from django.db import models
from django.conf import settings
from experiences.models import Experience

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user_order_number = models.PositiveIntegerField(null=True, blank=True)

    #each user will now have his own order counter and not the database one
    def save(self, *args, **kwargs):
        if not self.user_order_number:
            existing_orders_count = Order.objects.filter(user=self.user).count()
            self.user_order_number = existing_orders_count + 1
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} (User Order #{self.user_order_number})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    booking_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.experience.title} on {self.booking_date} (Order #{self.order.id})"