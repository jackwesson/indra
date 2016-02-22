from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Splash(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=500)
    

