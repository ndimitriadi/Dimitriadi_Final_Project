from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    # This makes the admin panel show "Categories" instead of "Categorys"
    class Meta:
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, blank=True, null=True)    
    description = models.TextField()
    image = models.ImageField(upload_to='experiences/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        
        if avg is not None:
            return round(avg, 1)  
        return 0.0 

#reviews
class Review(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.rating}-star review for {self.experience.title}"