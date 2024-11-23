from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)


    def __str__(self):
        return self.name



class Article(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title







