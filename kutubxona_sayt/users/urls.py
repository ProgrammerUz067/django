from django.urls import path
from .views import sign
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('signup/',sign,name='sig'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]


