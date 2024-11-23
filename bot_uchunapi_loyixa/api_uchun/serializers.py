from rest_framework import serializers
from .models import BotUser



class BotUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=BotUser
        fields="__all__"




