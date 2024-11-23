from django.shortcuts import render
from django.views.generic import ListView
from .models import Baho,Talaba,Fan
# Create your views here.


# def home(request):
#     return render(request,'home.html')


# class home(ListView):
#     template_name = "home.html"
#     model = Baho
#     context_object_name = "baholar"


# class talaba(ListView):
#     template_name = "talaba.html"
#     model = Talaba
#     context_object_name = "talaba"



# class fan(ListView):
#     template_name = "fan.html"
#     model = Fan
#     context_object_name = "fan"



def home(request):
    baholar=Baho.objects.all()
    context={
        "baholar":baholar
    }
    return render(request,"home.html",context)



def fan(request):
    fan=Fan.objects.all()
    fanlar_soni=Fan.objects.count()
    context={
        "fan":fan,
        "fanlar_soni":fanlar_soni
    }
    return render(request,"fan.html",context)



def talaba(request):
    talaba=Talaba.objects.all()
    tal_soni=Talaba.objects.count()
    context={
        "talaba":talaba,
        "tal_soni":tal_soni
    }
    return render(request,"talaba.html",context)
