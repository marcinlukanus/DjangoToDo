from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class ToDos(models.Model):
    todo = models.CharField(max_length=200)
    date_to_finish = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse('website-home')
