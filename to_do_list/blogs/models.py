from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ToDo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    is_finished=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user}-{self.title}"











