from .views import category_view, AddcategoryView, CategoryDetailView, product_view, Addprodukt, SearchPro, single
from django.urls import path

urlpatterns=[
    path("category/",category_view,name="page_category"),
    path("add_cat/",AddcategoryView,name="addcat"),
    path("add_pro/",Addprodukt,name="addpro"),
    path('search/', SearchPro, name='qidir'),
    path('product/single/<slug:category_slug>/<slug:product_slug>/',single, name='single_product'),
    path("product/",product_view,name="pro"),
    path("category/detail/<str:slug>/",CategoryDetailView,name="detcat"),

]
