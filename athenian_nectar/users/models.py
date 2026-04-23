from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    favorites = models.ManyToManyField('experiences.Experience', blank=True, related_name='favorited_by')    
    def __str__(self):
        return f'{self.user.username} Profile'