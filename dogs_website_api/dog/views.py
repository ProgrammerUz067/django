from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import DogSerializer
from .models import Dog

# Create your views here.


class DogSerializerView(CreateAPIView):
    model=Dog
    serializer_class = DogSerializer
    queryset = "dogs"





class DogView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer