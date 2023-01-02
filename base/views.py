from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  

from .models import Task, UsersSettings
from django.core.exceptions import PermissionDenied

def apply_settings(self, context):
  context['users_settings'] = UsersSettings.objects.filter(user=self.request.user)[0]
  return context

class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('tasks')

class RegisterPage(FormView):
  template_name = 'base/register.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('tasks')

  def form_invalid(self, form):
    return super().form_invalid(form)

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      new_users_settings = UsersSettings(user=user)
      new_users_settings.save()
      login(self.request, user)
    return super(RegisterPage, self).form_valid(form)
  
  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('tasks')
    return super(RegisterPage, self).get(*args, **kwargs) 


class TaskList(LoginRequiredMixin, ListView):
  model = Task
  context_object_name = 'tasks'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tasks'] = context['tasks'].filter(user=self.request.user)

    search_input = self.request.GET.get("search-area") or ''
    if search_input:
      context['tasks'] = context['tasks'].filter(title__icontains=search_input)

    context['count'] = context['tasks'].filter(complete=False).count()
    context['totalcount'] = context['tasks'].count()
    context['search_input'] = search_input

    context['display_settings'] = True
    return apply_settings(self, context)

class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'base/task.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if context.task.user != self.request.user:
      raise PermissionDenied()
    return apply_settings(self, context)

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title', 'description', 'complete']
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(TaskCreate, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return apply_settings(self, context)

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title', 'description', 'complete']
  success_url = reverse_lazy('tasks')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if context["task"].user != self.request.user:
      raise PermissionDenied()
    return apply_settings(self, context)

class DeleteView(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if context['task'].user != self.request.user:
      raise PermissionDenied()
    return apply_settings(self, context)

def toggleTaskCompleted(request):
  requestedTaskId = request.GET.get('id')
  if Task.objects.filter(user=request.user, id=requestedTaskId).exists():
    task = Task.objects.get(user=request.user, id=requestedTaskId)
    task.complete = not task.complete
    task.save()
  return redirect('tasks')
  
def themeChangeView(request):
  if UsersSettings.objects.filter(user=request.user).exists():
    settings = UsersSettings.objects.get(user=request.user)
    settings.darkmode = not settings.darkmode
    settings.save()
  return redirect('tasks')
  
def contrastChangeView(request):
  if UsersSettings.objects.filter(user=request.user).exists():
    settings = UsersSettings.objects.get(user=request.user)
    settings.high_contrast = not settings.high_contrast
    settings.save()
  return redirect('tasks')
  
def toggleHideCompleted(request):
  if UsersSettings.objects.filter(user=request.user).exists():
    settings = UsersSettings.objects.get(user=request.user)
    settings.hide_completed = not settings.hide_completed
    settings.save()
  return redirect('tasks')