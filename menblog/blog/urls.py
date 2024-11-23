from django.urls import path
from .views import home,alo,men


urlpatterns=[
    path("",home,name="saxifa"),
    path("concakt/",alo,name="aloqa"),
    path('about',men,name='men'),
]
