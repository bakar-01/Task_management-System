from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, ProfileUpdateForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    # Prevent editing if assigned to user by admin
    if not request.user.is_superuser and task.user != request.user:
        messages.error(request, 'You do not have permission to edit this task.')
        return redirect('task_list')
    if not request.user.is_superuser and task.user == request.user and task.user_created_by_admin():
        messages.error(request, 'You cannot edit tasks assigned to you by the admin.')
        return redirect('task_list')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

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
    task_list = Task.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(task_list, 5)  # Show 5 tasks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tasks/task_list.html', {'tasks': page_obj})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # If admin is assigning task to another user, set assigned_by to admin
            if request.user.is_superuser and 'user' in form.cleaned_data and form.cleaned_data['user'] != request.user:
                task.assigned_by = request.user
            else:
                task.assigned_by = None
            task.user = form.cleaned_data.get('user', request.user)
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    # Prevent deleting if assigned to user by admin
    if not request.user.is_superuser and task.user != request.user:
        messages.error(request, 'You do not have permission to delete this task.')
        return redirect('task_list')
    if not request.user.is_superuser and task.user == request.user and task.user_created_by_admin():
        messages.error(request, 'You cannot delete tasks assigned to you by the admin.')
        return redirect('task_list')

@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=user)
    return render(request, 'tasks/profile_update.html', {'form': form})
