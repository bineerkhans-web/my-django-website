from django.db import models

# Create your models here.
class User_registration(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    password=models.CharField(max_length=20,blank=True,null=True)

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name