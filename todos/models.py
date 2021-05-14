from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Todo(models.Model):

    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} - {self.user.username}'
