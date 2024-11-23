from django.db import models

# Create your models here.

class OziqOvqat(models.Model):
    name=models.CharField(max_length=255)
    ishlab_chiqaruvchi=models.TextField()
    narxi=models.IntegerField()
    yaroqlilik_mudati=models.IntegerField()
    rangi=models.CharField(max_length=100)







