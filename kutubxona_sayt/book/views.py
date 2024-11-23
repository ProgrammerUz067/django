from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,'index.html')

@login_required()
def aloqa(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')

@login_required()
def list(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,'books-media-gird-view-v2.html',context)

@login_required()
def new(request):
    return render(request,'news-events-list-view.html')


def fo(request):
    return render(request,'404.html')


def BlogDetail(request):
    return render(request,'blog-detail.html')


def books_media_detail(request):
    return render(request,'books-media-detail-v1.html')



def books_gird(request):
    return render(request,'books-media-gird-view-v1.html')

@login_required()
def cart(request):
    return render(request,'cart.html')

@login_required()
def chekout(request):
    return render(request,'cart.html')


def home2(request):
    return render(request,'home-v2.html')


def news2(request):
    return render(request,'news-events-detail.html')



@login_required()
def Bookdeteil(request,id):
    book=get_object_or_404(Book,id=id)
    context={
        "book":book
    }
    # return render(request,"detail.html",context)
    return render(request,"books-media-detail-v2.html",context)


