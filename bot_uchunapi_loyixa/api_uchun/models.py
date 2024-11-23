from django.db import models

# Create your models here.



class BotUser(models.Model):
    fuul_name=models.CharField(max_length=150,null=True,blank=True)
    user_name=models.CharField(max_length=150,null=True,blank=True)
    telegram_id=models.CharField(max_length=150,null=True,blank=True)



    def __str__(self):
        return self.fuul_name


