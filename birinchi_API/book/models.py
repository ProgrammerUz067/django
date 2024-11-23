from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    body=models.TextField()


    def __str__(self):
        return self.name






