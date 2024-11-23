from django.urls import path
from .views import home,delete_todo


urlpatterns=[
    path('',home,name='saxifa'),
    path('delete/<int:pk>/',delete_todo,name='delete_todo'),

]



