from django.db import models
from users.models import CustomUser


# Create your models here.

class Avto(models.Model):
    avto_name=models.CharField(max_length=255)
    motor=models.CharField(max_length=10)
    compani=models.CharField(max_length=255)
    mony=models.CharField(max_length=255)
    color=models.CharField(max_length=15)



class AvtoReview(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    avto=models.ForeignKey(Avto, on_delete=models.CASCADE)
    comment=models.TextField()














