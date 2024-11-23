from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title



class Post(models.Model):
    title=models.CharField(max_length=250)
    body=models.TextField()
    image=models.ImageField(upload_to='post_images')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

