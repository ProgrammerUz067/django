from django.urls import path
from .views import home,fol
urlpatterns = [
    path("home/",home,name='bosh'),
    path("flower/",fol,name='folwer_shop'),

]


