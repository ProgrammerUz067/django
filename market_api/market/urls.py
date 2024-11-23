from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import OziqlistApiView




urlpatterns=[
    path('product/',OziqlistApiView.as_view(),name='oziqovqat'),
]

