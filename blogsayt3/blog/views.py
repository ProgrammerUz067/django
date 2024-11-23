from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    yangilik=Blog.objects.all()
    context={
        "yangilik":yangilik
    }
    return render(request,"home.html",context)

