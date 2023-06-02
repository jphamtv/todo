# tasks/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = [
        "title",
        "description",
        "due_date",
    ]
    template_name = "task_edit.html"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_new.html"
    fields = (
        "title",
        "description",
        "due_date",
    )
