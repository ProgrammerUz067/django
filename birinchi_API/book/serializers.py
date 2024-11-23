from .models import Book,Category
from rest_framework import serializers

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'


class Categoryserialzer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'



class Bookdetailserializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"




