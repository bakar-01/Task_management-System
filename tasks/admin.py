from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'assigned_by', 'priority', 'deadline', 'completed')
    list_filter = ('priority', 'completed', 'category')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('deadline',)
    readonly_fields = ('created_at',)
    list_editable = ('completed', 'priority')

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'category')
        }),
        ('Assignment', {
            'fields': ('user', 'assigned_by')
        }),
        ('Status', {
            'fields': ('priority', 'deadline', 'completed')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

    class Media:
        css = {
            'all': ('tasks/css/admin_custom.css',)
        }

admin.site.register(Task, TaskAdmin)
