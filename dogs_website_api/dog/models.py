
from django.db import models






class Dog(models.Model):
    dog_images=models.ImageField(upload_to="image")
    dog_name=models.CharField(max_length=255)

    def __str__(self):
        return self.dog_name





