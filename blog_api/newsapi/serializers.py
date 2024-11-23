from .models import Category,News
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class NewsSerializers(ModelSerializer):
    class Meta:
        model=News
        fields="__all__"

