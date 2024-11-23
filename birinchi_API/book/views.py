from django.shortcuts import render

# Create your views here.
from .serializers import BookSerializers,Categoryserialzer,Bookdetailserializers
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Book,Category



class BookAPIview(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers



class CategoryAPIview(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserialzer


class BookDeatilAPIview(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookdetailserializers



