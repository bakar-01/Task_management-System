from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('profile_update/', views.profile_update, name='profile_update'),
]
