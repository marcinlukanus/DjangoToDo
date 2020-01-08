from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView
)
from .models import ToDos


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


class ToDoListView(ListView):
    model = ToDos
    template_name = 'website/home.html'
    context_object_name = 'todos'
    ordering = ['date_to_finish']


class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDos
    fields = ['todo', 'date_to_finish']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ToDosDetailView(DetailView):
    model = ToDos
