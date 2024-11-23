from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import OziqOvqat


class OziqOvqatSerializer(ModelSerializer):
    class Meta:
        model=OziqOvqat
        fields="__all__"






