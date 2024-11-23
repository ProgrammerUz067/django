from django.urls import path
from .views import SignupView
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('signup/',SignupView,name='sig'),
    path('login/',LoginView.as_view(),name='login'),
]