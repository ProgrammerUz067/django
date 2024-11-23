from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def news(request):
    return render(request,"news.html")


def con(request):
    return render(request,"aloqa.html")

def sport(request):
    return render(request,"sport.html")

def texno(request):
    return render(request,"texno.html")


def jaxon(request):
    return render(request,"jaxon.html")






