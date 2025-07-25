from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)   # Owner of the task
    assigned_by = models.ForeignKey(User, null=True, blank=True, related_name='assigned_tasks', on_delete=models.SET_NULL)  # Who assigned the task
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # New field for task details
    category = models.CharField(max_length=100, blank=True)    # New field for category/tag
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def user_created_by_admin(self):
        # Returns True if this task was assigned to a user by the admin (superuser)
        return self.assigned_by and self.assigned_by.is_superuser

    def __str__(self):
        return f"{self.title} ({self.priority})"
