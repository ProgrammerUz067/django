from django.shortcuts import render
from .models import Flower


# Create your views here.

def home(request):
    return render(request,"home.html")



def fol(request):
    return render(request,"fol.html")


