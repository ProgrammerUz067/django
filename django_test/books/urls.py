from django.urls import path
from .views import AddBookView,home,DeleteBookView
urlpatterns = [
    path("",home,name='saxifa'),
    path("addbook/",AddBookView,name='book_add'),
    path('deletbook',DeleteBookView,name='delbook'),

]


