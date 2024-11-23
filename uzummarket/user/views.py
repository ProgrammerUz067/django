from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from product.models import Products,Category
# Create your views here.

#bosh saxifa uchun
def home(request):
    return render(request,'home.html')



#userlar uchun
def login_page(request):
    if request.user.is_authenticated:
        messages.warning(request,"Siz allaqachon ro'yxatdan otgansiz")
        return redirect("saxifa")
    else:
        if request.method=="POST":
            forms=LoginForm(request.POST)
            if forms.is_valid():
                username=forms.cleaned_data["username"]
                password=forms.cleaned_data["password"]
                user=authenticate(request,username=username,password=password)
                login(request,user)
                messages.success(request,"Siz saytga muofaqiyatli kirdingiz !!")
                return redirect("saxifa")
        else:
            forms=LoginForm

        context={
            "forms":forms
        }
    return render(request,'users/login.html',context)



def signup(request):
    forms=UserRegisterForm
    if request.method=="POST":
        forms=UserRegisterForm(request.POST)
        if forms.is_valid():
            user=forms.save(commit=False)
            user.password = make_password(forms.cleaned_data['password1'])
            user.save()
            messages.success(request, "Saytdan ro'yxatdan o'ttingiz ")
            return redirect("login")
    context={
        "forms":forms
    }

    return render(request,'users/signup.html',context)



def user_logout(request):
    logout(request)
    return redirect('login')









