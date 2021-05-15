from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


# Create your views here.


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todos"

    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by("completed", "-date_created")


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo

    success_url = '/'

    def test_func(self):
        todo = self.get_object()

        if self.request.user == todo.user:
            return True

        return False

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


@login_required()
def todo_update_status(request, todo_id):

    todos = Todo.objects.filter(user=request.user)
    todo = get_object_or_404(todos, pk=todo_id)

    todo.completed = not todo.completed

    todo.save()

    messages.success(request, "Successfully updated status!")

    return redirect('todos:home')
