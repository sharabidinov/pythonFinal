from django.shortcuts import render, redirect
from .models import Task
from .models import Info
from .forms import TaskForm 


def mainp(request):
	tasks = Task.objects.order_by('-id')
	return render(request,"main/mainp.html", {'title': 'Главная страница', 'tasks': tasks})



def about(request):
	infos = Info.objects.all()
	return render(request,"main/about.html", {'inf': 'Про именинника', 'infos': infos})


def create(request):
	return render(request,"main/create.html")


def create(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			erroe = 'Некоректно'


	form = TaskForm()
	context = {
		'form': form,
		'error': error

	}
	return render(request,"main/create.html", context)