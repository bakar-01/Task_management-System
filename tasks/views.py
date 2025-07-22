from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Only current user's tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        deadline = request.POST.get('deadline')

        Task.objects.create(
            user=request.user,
            title=title,
            priority=priority,
            deadline=deadline
        )
        return redirect('task_list')

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')
