from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'index.html')


class Aloqa(TemplateView):
    template_name = "contact.html"



class About(TemplateView):
    template_name = "about.html"

