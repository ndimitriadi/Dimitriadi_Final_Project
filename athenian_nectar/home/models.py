from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    stars = models.IntegerField(default=5)

    def __str__(self):
        return self.name