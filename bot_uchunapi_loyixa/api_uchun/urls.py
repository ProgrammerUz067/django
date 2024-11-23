from django.urls import path
from .views import CreateBotApiView
urlpatterns = [
    path('creat/',CreateBotApiView.as_view()),
]