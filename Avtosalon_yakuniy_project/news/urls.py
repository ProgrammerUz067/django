from .views import home,aloqa,AvtoListView
from django.urls import path


urlpatterns=[
    path('',home,name='home'),
    path('contact',aloqa,name='alo'),
    path('api/v1/avtolist',AvtoListView.as_view()),
]



