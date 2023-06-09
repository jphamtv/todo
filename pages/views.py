# pages/views.py
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = reverse_lazy('login')

    # If user is authenticated, navigate to the tasks list
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('task_list')
        else:
            return super().get(request, *args, **kwargs)