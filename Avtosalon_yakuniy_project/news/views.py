from django.shortcuts import render
from .models import Avto
from rest_framework.generics import ListAPIView
from .serializers import AvtoApiSerializer


class AvtoListView(ListAPIView):
    queryset = Avto.objects.all()
    serializer_class = AvtoApiSerializer



def home(request):
    lates_new = Avto.objects.order_by('-id').first()
    news = Avto.objects.order_by('-id')[:5]
    chevrolet = Avto.objects.filter(category__name="Chevrolet")
    bmw = Avto.objects.filter(category__name="Bmw")
    mers = Avto.objects.filter(category__name="Mers")
    context={
        "lates_new":lates_new,
        "news":news,
        "chevrolet":chevrolet,
        "bmw":bmw,
        "mers":mers,

    }
    return render(request,'index.html',context)






def aloqa(request):
    return render(request,'contact.html')

