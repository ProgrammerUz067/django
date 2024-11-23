from django.shortcuts import render
from .models import Blog,Post
from django.views.generic import TemplateView,ListView
#Bosh saxifa uchun views

def home(request):
    yangiliklar=Blog.objects.all()
    context = {
        "x":yangiliklar
    }
    return render(request,"home.html",context)

class Aloqa(TemplateView):
    template_name = "contact.html"



class ListsPost(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'



