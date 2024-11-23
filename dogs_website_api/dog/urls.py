from django.urls import path
from .views import DogSerializerView,DogView
urlpatterns = [
    path('dog/',DogSerializerView.as_view()),
    path('dogs/',DogView.as_view()),
]
