from django.db import models

# Create your models here.


class Categoriya(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
       return self.name


class Avto(models.Model):
    categoriya=models.ForeignKey(Categoriya,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    color=models.CharField(max_length=100)
    mator=models.IntegerField()
    price=models.IntegerField()
    kompaniya=models.CharField(max_length=255)

    def __str__(self):
       return self.name


