# project_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path("", views.dashboard, name="dashboard"),
  path('projects/', views.get_project_list, name='project-list'),
  path('projects/create/', views.create_project, name='project-create'),
  path('projects/<int:pk>/', views.get_project, name='project-detail'),
  path('projects/<int:pk>/update/', views.update_project, name='project-update'),
  path('projects/<int:pk>/delete/', views.delete_project, name='project-delete'),
]
