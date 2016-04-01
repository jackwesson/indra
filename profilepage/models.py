from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.conf import settings



# Create your models here.
class profile(models.Model):
    owner = models.ForeignKey(User, related_name="profile_picture")
    profilepicture = models.ImageField(upload_to='uploads/')
    
    
    
class music(models.Model):
    owner = models.ForeignKey(User, related_name="example_music")
    examplemusic = models.FileField(upload_to='uploads/')