from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def home(request):
		return render(request, 'todo/home.html')

def dashboard(request):
		tasks = Task.objects.all()
		form = TaskForm()

		if request.method == 'POST':
			form = TaskForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect('/dashboard/')

		context_dict = {'tasks':tasks, 'form':form}
		return render(request, 'todo/dashboard.html', context_dict)

def update(request, key):
	task = Task.objects.get(id=key)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('/dashboard/')

	context_dict = {'form':form}
	return render(request, 'todo/update.html', context_dict)

def delete(request, key):
	task = Task.objects.get(id=key)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		task.delete()
		return redirect('/dashboard/')

	context_dict = {'task':task}
	return render(request, 'todo/delete.html', context_dict)

