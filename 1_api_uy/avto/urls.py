from .views import AvtoView,CategoryView,AvtoDetailView
from django.urls import path




urlpatterns=[
    path('api/v1/avtolist',AvtoView.as_view()),
    path('api/v1/categorylist',CategoryView.as_view()),
    path('api/v1/category/<int:pk>/',AvtoDetailView.as_view()),
]


