from rest_framework import serializers
from .models import Avto,Categoriya

class AvtoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Avto
        fields = '__all__'





class CategoriyaSerializers(serializers.ModelSerializer):
    class Meta:
        model:Categoriya
        fields='__all__'



class AvtoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model:Avto
        fields='__all__'


