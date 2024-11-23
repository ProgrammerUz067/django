from .models import Avto,Category
from rest_framework.serializers import ModelSerializer



class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"



class AvtoApiSerializer(ModelSerializer):
    class Meta:
        model=Avto
        fields="__all__"

