from django.urls import path
from .views import home,add,cat

urlpatterns=[
    path('',home,name='saxifa'),
    path('add/',add,name='photo'),
    path('ca/',cat,name='co'),
]





