from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import BotUserSerializers
from .models import BotUser

# Create your views here.


class CreateBotApiView(CreateAPIView):
    model=BotUser
    serializer_class = BotUserSerializers
    queryset = "users"















