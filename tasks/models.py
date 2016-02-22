from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey(User, related_name="owned_tasks")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    collaborators = models.ManyToManyField(User, related_name="tasks")
    complete = models.BooleanField(default = False)