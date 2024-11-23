from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import AddBookForm
from django.contrib import messages
# Create your views here.




def home(request):
    return render(request,'home.html')




def AddBookView(request):
    forms=AddBookForm()
    if request.method=="POST":
        forms=AddBookForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Kitob qo'shildi")
            return redirect("home.html")
    context={
        "forms":forms
    }
    return render(request,"add_book.html",context)





def DeleteBookView(request):
   book = get_object_or_404(Book)
   if request.method=="POST":
       book.delete()
       return redirect('home')
   context={
        "book":book,
   }
   return render(request,'delet.html',context)


