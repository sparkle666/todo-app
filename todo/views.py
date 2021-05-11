from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
	todo = Todo.objects.order_by('id')
	form = TodoForm()
	context = {'todo_items': todo, 'form': form}
	return render(request, 'todo/index.html', context)

@require_POST # To ensure this view only accept a POST request and not a GET request
def addTodo(request):
	form = TodoForm(request.POST)
	if form.is_valid():
		todo_item = Todo(text = request.POST['text'])
		todo_item.save()
	return redirect('index')

def complete(request, todo_id):
	'''Gets the ID from URL, sets it to completed and and save it.'''
	todo_item = Todo.objects.get(id = todo_id)
	todo_item.completed = True
	todo_item.save()
	return redirect('index')

def deletecompleted(request):
	""" Delete all completed todo items from the database... Fetch them and delete."""
	Todo.objects.filter(completed__exact = True).delete()
	return redirect('index')

def delete_all(request):
	Todo.objects.all().delete()
	return redirect('index')
