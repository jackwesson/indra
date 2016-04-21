from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.conf import settings


# Create your models here.

class connection(models.Model):
    target = models.ForeignKey(User, related_name="target")
    originator = models.ForeignKey(User, related_name="originator")
    accepted = models.BooleanField(default = False)