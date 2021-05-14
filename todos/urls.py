from django.urls import path
from .views import home

app_name = "todos"

urlpatterns = [
    path("", home, name="home"),
]
