from django.db import models




class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name





class Avto(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="news_images/")
    price=models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title


