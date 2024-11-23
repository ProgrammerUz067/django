from django.urls import path
from .views import home,Aloqa,About
# from . import views



urlpatterns=[
    path('',home,name='saxifa'),
    path("aloqa/",Aloqa.as_view(),name="alo"),
    path('about/',About.as_view(),name='haqida'),
]

