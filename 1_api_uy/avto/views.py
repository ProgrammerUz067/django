from django.shortcuts import render


from .serializers import AvtoSerializers,CategoriyaSerializers,AvtoDetailSerializers
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Avto,Categoriya



# Create your views here.



class AvtoView(ListAPIView):
    queryset =Avto.objects.all()
    serializer_class =AvtoSerializers


class CategoryView(ListAPIView):
    queryset = Categoriya.objects.all()
    serializer_class = CategoriyaSerializers


class AvtoDetailView(ListAPIView):
    queryset = Avto.objects.all()
    serializer_class =AvtoDetailSerializers










