from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    created_by = models.ForeignKey(User)
    text = models.CharField(max_length=140)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
