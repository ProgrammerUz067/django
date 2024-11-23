from django.db import models

# Create your models here.


class User(models.Model):
    phone_num=models.IntegerField
    password=models.IntegerField(max_length=8 ,null=False)
    user_name=models.CharField(max_length=150, null=True, blank=True)
    photo_user=models.ImageField(upload_to='user_image/', null=True, blank=True)


    def __str__(self):
        return f"{self.user_name},{self.phone_num}"





