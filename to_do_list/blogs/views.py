from django.shortcuts import render, get_object_or_404
from .models import ToDo

# Create your views here.

def home(request):
    todos=ToDo.objects.filter(user=request.user)
    context={
        "todos":todos
    }
    return render(request,'home.html',context)



def delete_todo(request,pk=None):
    todo=get_object_or_404(ToDo,id=pk)
    todo.delet()
    return render('todohome')






