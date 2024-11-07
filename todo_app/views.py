from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = task.objects.all()
    
    form = taskForm()

    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    # return HttpRespons e('Hello World')
    return render(request, 'todo_app/index.html', context)

def modifyTask(request, pry_key):
    Task = task.objects.get(id=pry_key)

    form = taskForm(instance=Task)

    if request.method == 'POST':
        form = taskForm(request.POST, instance=Task)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}

    return render(request, 'todo_app/modify.html', context)  


def deleteTask(request, pry_key):
    item = task.objects.get(id=pry_key)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todo_app/delete.html', context)