from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, themeChangeView, toggleHideCompleted, toggleTaskCompleted, contrastChangeView, toggleFilterByDeadline, UserSettingssUpdate, readmeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
  path('register/', RegisterPage.as_view(), name='register'),


  path('', TaskList.as_view(), name='tasks'),
  path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
  path('task-create/', TaskCreate.as_view(), name='task-create'),
  path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
  path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
  path('task-toggle-status/', toggleTaskCompleted, name='task-toggle-status'),

  path('changetheme/', themeChangeView, name='theme'),
  path('changecontrast/', contrastChangeView, name='contrast'),
  path('hide_completed/', toggleHideCompleted, name='hide_completed'),
  path('filter_by_deadline/', toggleFilterByDeadline, name='filter_by_deadline'),
  path('users_display_after_date/<int:pk>/', UserSettingssUpdate.as_view(), name='users_display_after_date'),
  

  path('readme', readmeView, name='readme')
]