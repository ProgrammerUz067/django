from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os


def get_file_path(request,filename):
    or_file=filename
    nowtime=datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s"%(nowtime,or_file)

    return os.path.join('uploads/',filename)


class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="O=defoult 1=Midden")
    trending=models.BooleanField(default=False,help_text="0=defoult 1-trending")
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name_plural="Kategoriya"



    def __str__(self):
        return self.name



class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=False,blank=False)
    small_description=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False,help_text="Mahsulot miqdori")
    description=models.TextField(max_length=500,null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=True,blank=False)
    status=models.BooleanField(default=False,help_text="0=default 1=Midden")
    trending=models.BooleanField(default=False,help_text="0=default 1=Midden")
    tag=models.CharField(max_length=150,null=False,blank=False)
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.TextField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Mahsulot"


    def __str__(self):
        return self.name







class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.product.name} mahsulotidan | {self.product_qty} dona tanladi"











