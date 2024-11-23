from django.urls import path
from .views import home,Aloqa,ListsPost


urlpatterns=[
    path("",home,name="saxifa"),
    path("aloqa/",Aloqa.as_view(),name="tel"),
    path("post/",ListsPost.as_view(),name="news"),
]


