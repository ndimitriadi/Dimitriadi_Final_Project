from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=50, unique=True) 
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True) 

