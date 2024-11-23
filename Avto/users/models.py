from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    photo_user=models.ImageField(upload_to='user_image/',null=True,blank=True)
    age=models.CharField(max_length=115)








