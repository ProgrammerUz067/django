from django.urls import path
from .views import home,talaba,fan



urlpatterns=[
    path('',home,name='bosh'),
    path('talaba/',talaba,name="talaba"),
    path("fan/",fan,name="fan"),
]




