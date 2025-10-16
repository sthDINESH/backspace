from django.urls import path
from . import views

urlpatterns = [
    path('workspaces/', views.workspace_list, name='workspace_list'),
]