from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=155)
    email=models.EmailField()
    number=models.CharField(max_length=17)
    message=models.TextField()


    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title






