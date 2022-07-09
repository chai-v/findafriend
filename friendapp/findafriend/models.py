from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    interests = models.CharField(max_length=150)
    color = models.CharField(max_length=30)
    food = models.CharField(max_length=30)
    hobby = models.CharField(max_length=30)
    age = models.IntegerField()