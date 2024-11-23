from django.urls import path
from .views import home,aloqa,men,pos

urlpatterns=[
    path('',home.as_view(),name='saxifa'),
    path('aloqa/',aloqa,name='alo'),
    path('about/',men.as_view(),name='men'),
    path('post/',pos.as_view(),name='post'),
]



