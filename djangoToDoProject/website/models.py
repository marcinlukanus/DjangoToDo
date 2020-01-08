from django.db import models
from django.contrib.auth.models import User


class ToDos(models.Model):
    todo = models.CharField(max_length=200)
    date_to_finish = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo
