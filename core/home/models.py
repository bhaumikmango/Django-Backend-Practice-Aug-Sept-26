from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() # Automatically created by django
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class Product(models.Model):
    pass