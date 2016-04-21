from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.conf import settings



# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, related_name="profile_picture")
    profilepicture = models.ImageField(upload_to="propics")
    
class music(models.Model):
    owner = models.ForeignKey(User, related_name="example_music")
    examplemusic = models.FileField(upload_to='uploads/')
    
class description(models.Model):
    owner = models.ForeignKey(User, related_name="band_name", primary_key = True)
    blurb = models.CharField(max_length=100)


    