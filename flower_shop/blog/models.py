from django.db import models

# Create your models here.

class Flower(models.Model):
    name=models.CharField(max_length=255)
    img=models.ImageField()
    decription=models.TextField()
    price=models.TextField(max_length=100)



def __str__(self):
    return self.name