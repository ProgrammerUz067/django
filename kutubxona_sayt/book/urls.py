from django.urls import path
from .views import home,aloqa,blog,list,new,fo,BlogDetail,books_media_detail,books_gird,cart,chekout,home2,news2,Bookdeteil

urlpatterns=[
    path('',home,name='saxifa'),
    path('aloqa/',aloqa,name='alo'),
    path('blog/',blog,name='blog'),
    path('list/',list,name='book'),
    path('new/',new,name='news'),
    path('404/',fo,name='for'),
    path('BlogDetail/',BlogDetail,name='BlogD'),
    path('books_detail/',books_media_detail,name='mediabooks'),
    path('books_gird/',books_gird,name='book_gird'),
    path('cart/',cart,name='cart1'),
    path('chekout/',chekout,name='chekout1'),
    path('home2/',home2,name='home1'),
    path('news2/',news2,name='new2'),
    path('detail/<int:id>/',Bookdeteil,name='book_detail'),
]



