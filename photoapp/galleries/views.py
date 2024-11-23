from django.shortcuts import render,reverse,redirect
from .models import Category,Photo
from .forms import Add,Addcat
# Create your views here.


def home(request):
    categories=Category.objects.all()
    photo=Photo.objects.all()
    context={
        'categories':categories,
        'photos':photo
    }
    return render(request,'home.html',context)




def add(request):
    form=Add()
    if request.method=='POST':
        form=Add(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('saxifa')
    context={
        'form':form
    }
    return render(request,'add.html',context)


def cat(request):
    form=Addcat()
    if request.method=="POST":
        form=Addcat(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saxifa')
    context={
        "form":form
    }
    return render(request,"cat.html",context)









