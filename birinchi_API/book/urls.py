from .views import BookAPIview,CategoryAPIview,BookDeatilAPIview
from django.urls import path



urlpatterns = [
    path('api/v1/booklist',BookAPIview.as_view()),
    path('api/v2/categorylist',CategoryAPIview.as_view()),
    path('api/v3/bookdeatil/<int:pk>/',BookDeatilAPIview.as_view()),
]





