from django.urls import path
from .views import ArticleView,ArcitleDeleteView,CreateView,ArticleUptateView,CategoryView,CategoryDeletView,CreateCategoryView,CategoryUpdateView
from .views import ArticleViewSet
from rest_framework.routers import SimpleRouter

router=SimpleRouter()

router.register("article",ArticleViewSet,basename="new")

urlpatterns=[
    # path('api/v1/list',ArticleView.as_view()),
    # path('api/v1/deletlist/<int:pk>/',ArcitleDeleteView.as_view()),
    # path('api/v1/update/<int:pk>/',ArticleUptateView.as_view()),
    # path('api/v1/create',CreateView.as_view()),
    # path('api/v1/category',CategoryView.as_view()),
    # path('api/v1/deletcategory/<int:pk>/', CategoryDeletView.as_view()),
    # path('api/v1/createcategory', CreateCategoryView.as_view()),
    # path('api/v1/updatecategory/<int:pk>/', CategoryUpdateView.as_view()),\

]

urlpatterns+=router.urls



