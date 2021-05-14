from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ModelListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todos"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by("-date_created")
