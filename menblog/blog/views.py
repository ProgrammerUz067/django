from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,"home.html")





def alo(request):
    return render(request,"aloqa.html")


def men(request):
    return render(request,"men_ha.html")




