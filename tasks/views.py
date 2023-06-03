# tasks/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    template_name = "task_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = [
        "title",
        "description",
        "due_date",
    ]
    template_name = "task_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_new.html"
    fields = (
        "title",
        "description",
        "due_date",
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
