from django.urls import path
from .views import ModelListView

app_name = "todos"

urlpatterns = [
    path("", ModelListView.as_view(), name="home"),
]
