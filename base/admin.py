from django.contrib import admin
from .models import Task, UsersSettings

admin.site.register(Task)
admin.site.register(UsersSettings)