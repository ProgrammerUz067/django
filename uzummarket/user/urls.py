from django.urls import path
from .views import home,signup,login_page,user_logout
urlpatterns = [
    path('',home,name='saxifa'),
    path('sigin/',signup,name='sig'),
    path('login/',login_page,name='login'),
    path('logout/', user_logout, name='logout'),

]
