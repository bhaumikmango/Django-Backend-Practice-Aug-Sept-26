from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() # Automatically created by django
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True, blank = True)
    image = models.ImageField()
    file = models.FileField()

class Car(models.Model):
    name = models.CharField(max_length=150)
    speed = models.IntegerField(default=64)

    def __str__(self):
        return self.name