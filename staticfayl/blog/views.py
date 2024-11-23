from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from .models import Post,Contact
from .forms import ContactForm
# Create your views  this

class home(ListView):
    template_name = 'index.html'
    model =Post
    context_object_name = "posts"





def aloqa(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saxifa')
    context={
        "form":form
    }
    return render(request,"contact.html",context)



class men(TemplateView):
    template_name = 'about.html'


class pos(TemplateView):
    template_name = 'post.html'


