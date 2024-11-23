from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewsSerializers
from .models import News
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView





# class NewsViewSet(ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializers


class NewsView(APIView):
    def delete(self, request,pk):
        new=News.objects.get(id=pk)
        new.delete()
        data={
            "status":True,
            "message":"Yangilik o'chirildi",
        }
        return Response(data)
