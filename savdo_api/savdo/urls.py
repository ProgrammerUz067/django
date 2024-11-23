from .views import ProductViewSet,CategoryViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path

router=SimpleRouter()

router.register("product",ProductViewSet,basename='narsa')
router.register("category",CategoryViewSet,basename='categoriya')

urlpatterns=router.urls
