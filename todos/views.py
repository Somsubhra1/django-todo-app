from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todos"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by("completed", "-date_created")


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo

    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Successfully deleted Todo!")
        return super().delete(request, *args, **kwargs)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title"]

    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successfully created Todo!")
        return super().form_valid(form)


def todo_update_status(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    todo.completed = not todo.completed

    todo.save()

    return redirect('todos:home')
