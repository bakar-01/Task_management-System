# Generated by Django 5.2.3 on 2025-07-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_deadline_task_priority_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
