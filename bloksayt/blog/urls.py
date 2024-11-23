from django.urls import path
from .views import home,news,con,sport,texno,jaxon

urlpatterns=[
    path("",home,name="sayt"),
    path("new/",news,name="news uzb"),
    path("contak/",con,name="tel"),
    path("sport/",sport,name="sport"),
    path("texnologiya/",texno,name='texno'),
    path("jaxon/",jaxon,name="jaxon"),
]







