from django.contrib import admin

# Register your models here.
from todo.models import Projects, ProjectsTodo


class ProjectsTodoAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['project', 'user', 'status', 'created_at', 'updated_at']
    list_filter = ['project', 'user', 'status']


admin.site.register(Projects)
admin.site.register(ProjectsTodo, ProjectsTodoAdmin)

