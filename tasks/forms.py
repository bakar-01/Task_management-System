from django import forms
from django.contrib.auth.models import User
from .models import Task

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'completed', 'priority', 'deadline', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Task Description'}),
            'category': forms.TextInput(attrs={'placeholder': 'Category'}),
            'completed': forms.CheckboxInput(),
            'priority': forms.Select(),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'user': forms.Select(),
        }
