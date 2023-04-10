from django.shortcuts import render, redirect
from django.db.models import F
from datetime import date
from .models import Todo

# Create your views here.
def home(request):
    Todos = Todo.objects.all().order_by(F("end_date").asc(nulls_last=True))
    today = date.today()
    for todo in Todos:
        todo.end_date = todo.end_date.date() -  today
        if not todo.end_date:
            todo.end_date = "0 days"
    return render(request, 'home.html', {'Todos': Todos})

def new(request):
    if request.method == "POST":
        new_Todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = request.POST['end_date']
        )
        return redirect('home')
    return render(request, 'new.html')

def detail(request, todo_pk):
    Todos = Todo.objects.filter(pk=todo_pk)
    return render(request, 'detail.html', {'Todos': Todos})

def update(request, todo_pk):
    Todos = Todo.objects.filter(pk=todo_pk)
    if request.method == "POST":
        Todo.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = request.POST['end_date']
            
        )
        return redirect('home')
    return render(request, 'update.html', {'Todos': Todos})   

def delete(request, todo_pk):
    Todos = Todo.objects.filter(pk=todo_pk)
    Todos.delete()
    return redirect('home')
