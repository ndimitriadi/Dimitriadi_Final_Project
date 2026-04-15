from django.db import models

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
        return f"{self.category.name} - {self.name}"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, blank=True, null=True)    
    description = models.TextField()
    image = models.ImageField(upload_to='experiences/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    total_reviews = models.IntegerField(default=0)


    def __str__(self):
        return self.title