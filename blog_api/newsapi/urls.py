from .views import NewsView
from rest_framework.routers import SimpleRouter
from django.urls import path

router=SimpleRouter()
router.register("news",NewsView,basename='yangiliklar')

urlpatterns=router.urls

