from django.db import models
from django.contrib.auth.models import User
from datetime import *
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete', '-deadline', 'created']


class UsersSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    darkmode = models.BooleanField(default=True)
    hide_completed = models.BooleanField(default=False)
    high_contrast = models.BooleanField(default=True)
    filter_by_deadline = models.BooleanField(default=True)
    users_display_after_date = models.DateTimeField(default = timezone.now)