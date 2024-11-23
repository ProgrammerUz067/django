from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect
from .forms import SignupForm
# Create your views here.

def sign(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST,files=request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(form.cleaned_data['password1'])
            user.save()
            return redirect('saxifa')
    context={
            'form':form
        }


    return render(request,'registration/signup.html',context)









