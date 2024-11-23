from django.db import models

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=200)


    def __str__(self):
        return self.name




class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    body=models.TextField()
    price=models.IntegerField()
    color=models.CharField(max_length=100)
    brend=models.TextField()


    def __str__(self):
        return self.title







