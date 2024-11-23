from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

#o'quvchilarning malumotlarini saqlash uchun model

class Talaba(models.Model):
    ism=models.CharField(max_length=255)
    familya=models.CharField(max_length=255)
    yosh=models.IntegerField(max_length=5)
    manzil=models.TextField()

    def __str__(self):
        return self.ism

#fanlar ro'yxatini saqlash uchun model
class Fan(models.Model):
    nomi=models.CharField(max_length=100)

    def __str__(self):
        return self.nomi



#talabaning bahosi
class Baho(models.Model):
    ism=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    fan=models.ForeignKey(Fan,on_delete=models.CASCADE)
    baho=models.IntegerField(
         validators=[
             MinValueValidator(1,message="1 balldan kam baho qo'yish mumkin emas"),
             MaxValueValidator(5,message="5 baldan katta baho qo'yish mumkin emas")
         ]
    )


    def __str__(self):
        return f"{self.ism} {self.fan} {self.baho}"




