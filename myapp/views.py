from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView

from myapp.models import Task  # Updated import statement


# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
